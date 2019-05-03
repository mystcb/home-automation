#!/usr/bin/python3
# MQTT Publish Script for Home Sensors - FlightRadar24
# ----------------------------------------------------
# by Colin Barker (colin@faereal.net)
#
# Connets to an MQTT server and publishes data set by
# the DUMP1090 device, attached to a Raspberry Pi 3

# Import all the modules required
import json
import uuid
import time
import paho.mqtt.client as mqtt
import argparse
import sys

# Setup arguments for use with the CLI
parser = argparse.ArgumentParser()
parser.add_argument('-C', '--config', required=True, default=str("config.json"), help="location of the config file (json)", metavar="file")

args, unknown = parser.parse_known_args()

# Bring in the config file
try:
    with open(str(args.config)) as config_file:
        data = json.load(config_file)
except FileNotFoundError as e:
    print("Error with configuration file: " + str(e))
    sys.exit(1)


# Functions for the mqtt.Client to callback to
# TODO: Switch these over for logging
def on_connect(mqttc, obj, flags, rc):
    print("connect rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected MQTT disconnection. Will auto-reconnect")

# Create a MQTT Client using the ClientID
client = mqtt.Client(data['clientId'])
client.username_pw_set(data['mqttUsername'],data['mqttPassword'])

# Set all the callback functions
client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Connect to the MQTT server using the above Client information
try:
        client.connect(data['mqttHost'])
except Exception as e:
        print("Error with connection: " + str(e))
        sys.exit(1)

# Start the loop
client.loop_start()

# Try while loop
try:
    while True:
        # Load up the aircraft file
        with open('/run/dump1090-mutability/aircraft.json') as aircraft_file:
            aircraft_data = json.load(aircraft_file)
        # Push the data
        #print('Aircraft Seen: ' + str(len(aircraft_data['aircraft'])))
        msg = client.publish(str(data['deviceName']) + "/tracked_aircraft", len(aircraft_data['aircraft']))
        time.sleep(5)
except KeyboardInterrupt:
    # If we interupt the process, push on and close the connnection
    pass

# Close out all the connections, and stop the loop
client.loop_stop()
client.disconnect()