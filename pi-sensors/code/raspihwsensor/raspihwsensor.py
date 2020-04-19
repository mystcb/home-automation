#!/usr/bin/python3
# MQTT Publish Script for Home Sensors
# ------------------------------------
# by Colin Barker (colin@faereal.net)
#
# Connets to an MQTT server and publishes data pulled from
# the Pi hardware, for example CPU and GPU temps

# Import all the modules required
import paho.mqtt.client as mqtt
import json
import time
import argparse
import uuid
import sys
import gpiozero # pylint: disable=import-error

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

# Connect to the MQTT server using the above Client information
try:
    client.connect(data['mqttHost'])
except Exception as e:
    print("Error with connection: " + str(e))
    sys.exit(1)

# Start the loop
client.loop_start()

# Exception catching for keyboard interupts.
try:
    while True:
        # Generate the payload data from gpiozero
        payload = "{{ \"temperature\": {0:.2f} }}".format(gpiozero.CPUTemperature().temperature)
        # Push the payload up to the MQTT Broker
        print("Pushing Payload: " + payload)
        msg = client.publish(str(data['deviceLocation']) + "/" + str(data['deviceName']) + "/system", payload)
        # Check to see if the messge was sent, print the error number if there is a problem
        if msg.rc != 0:
            print("Message not sent: " + str(msg.rc))
        # Sleep for the time required so we don't flood the MQTT broker
        time.sleep(int(data['reportInterval']))
except KeyboardInterrupt:
    # If we interupt the process, push on to close the connection
    pass

# Close out all the connections, and stop the loop
client.loop_stop()
client.disconnect()