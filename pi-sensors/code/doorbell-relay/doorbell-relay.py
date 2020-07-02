#!/usr/bin/python3
# MQTT Publish Script for Home Sensors
# ------------------------------------
# by Colin Barker (colin@faereal.net)
#
# Connets to an MQTT server and publishes data pulled from
# a bme680 chip, attached to a Raspberry Pi Zero W

# Import all the modules required
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO # pylint: disable=import-error
import json
import time
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

# Setup the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(int(data['gpioPin_button']), GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(int(data['gpioPin_relay']), GPIO.OUT, initial=1)

# Set the initial state of the doorbell button
bellPressed = False

# Exception catching for keyboard interupts.
try:
    while True:
        # Lets see if the button has been pressed
        if GPIO.input(int(data['gpioPin_button'])) == GPIO.LOW and bellPressed == False:
            print("Doorbell Pressed")
            bellPressed = True
            # Set the GPIO to 0 to cause the relay to switch ON
            GPIO.output(int(data['gpioPin_relay']),0)
            # Push Payload to MQTT
            msg = client.publish(str(data['deviceLocation']) + "/" + str(data['bellName']) + "/state", "ON", retain=True)
        if GPIO.input(int(data['gpioPin_button'])) == GPIO.HIGH and bellPressed == True:
            print('Reset')
            bellPressed = False
            # Set the GPIO to 1 to cause the relay to switch OFF
            GPIO.output(int(data['gpioPin_relay']),1)
            # Push Payload to MQTT
            msg = client.publish(str(data['deviceLocation']) + "/" + str(data['bellName']) + "/state", "OFF", retain=True)
        time.sleep(0.1)

except KeyboardInterrupt:
    # If we interupt the process, push on to close the connection
    pass

# Close out all the connections, and stop the loop
GPIO.cleanup()
client.loop_stop()
client.disconnect()