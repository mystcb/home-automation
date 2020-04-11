#!/usr/bin/python3
# MQTT Publish Script for Home Sensors - PIR
# ------------------------------------------
# by Colin Barker (colin@faereal.net)
#
# Connets to an MQTT server and publishes data set by
# a PIR Sensor, attached to a Raspberry Pi Zero W

# Import all the modules required
import RPi.GPIO as GPIO # pylint: disable=import-error
import json
import time
import paho.mqtt.client as mqtt
import argparse
import uuid
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
def on_connect(client, obj, flags, rc):
    print("connect rc: " + str(rc))
    client.publish(str(data['deviceLocation']) + "/" + str(data['pirName']) + "/status", "online")

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected MQTT disconnection. Will auto-reconnect")

# Create a MQTT Client using the ClientID
client = mqtt.Client(data['clientId'])
client.username_pw_set(data['mqttUsername'],data['mqttPassword'])
# Setup the "will_set" so that if it disconnects reset to this topic
client.will_set(str(data['deviceLocation']) + "/" + str(data['pirName']) + "/status", "offline")

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

# Setup the GPIO ports to listen in
GPIO.setmode(GPIO.BOARD)

data['gpioPin'] = 11

GPIO.setup(int(data['gpioPin']), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

stateMovement = False

try:
    while True:
        if GPIO.input(int(data['gpioPin'])) == GPIO.HIGH and stateMovement == False:
                print('Movement detected: ' + str(data['pirName']))
                stateMovement = True
                # Push Payload to MQTT
                client.publish(str(data['deviceLocation']) + "/" + str(data['pirName']) + "/status", "online")
                msg = client.publish(str(data['deviceLocation']) + "/" + str(data['pirName']) + "/state", "ON")
        if GPIO.input(int(data['gpioPin'])) == GPIO.LOW and stateMovement == True:
                print ('Movement stopped: ' + str(data['pirName']))
                stateMovement = False
                # Push Payload to MQTT
                client.publish(str(data['deviceLocation']) + "/" + str(data['pirName']) + "/status", "online")
                msg = client.publish(str(data['deviceLocation']) + "/" + str(data['pirName']) + "/state", "OFF")
        time.sleep(0.5)
except KeyboardInterrupt:
    # If we interupt the process, push on to close the connection
    pass

# Close out all the connections, and stop the loop, and publish the offline status
client.publish(str(data['deviceLocation']) + "/" + str(data['pirName']) + "/status", "offline")
client.loop_stop()
client.disconnect()