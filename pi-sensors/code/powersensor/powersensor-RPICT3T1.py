#!/usr/bin/python3
# MQTT Publish Script for Home Sensors - Power
# -----------------------------------------------
# by Colin Barker (colin@faereal.net)
#
# Connets to an MQTT server and publishes data set by
# RPICT3T1 Power Sensor, attached to a Raspberry Pi Zero W

# Import all the modules required
import sys
import argparse # pylint: disable=import-error
import json
import time
import paho.mqtt.client as mqtt # pylint: disable=import-error
import serial # pylint: disable=import-error


# Setup arguments for use with the CLI
parser = argparse.ArgumentParser()
parser.add_argument(
    '-C',
    '--config', 
    required=True, 
    default=str("config.json"), 
    help="location of the config file (json)", metavar="file")

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

# Setup the serial connection
ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=5)

# Main monitoring loop
try:
    while True:
        try:
            # Read in the whole line from the seial connector
            sensorData = ser.readline().decode("utf-8")
        except:
            time.sleep(5)
            continue
        # Split the serial readline using a space as a delimiter
        z = sensorData.split(" ")
        # Set the comma usage to False
        comma = False
        # Initial part of the Payload JSON
        payload = "{"
        # Loop over all entries from the delimited split
        for i in range(len(z)):
            # Check config, if sensor is enabled then continue
            if i in data['enableSensor']:
                # Check to see if a comma is required
                if comma:
                    payload += ", "
                # Generate the main part of the payload
                #print("Power usage on sensor %d: %s W" % (i,z[i]))
                payload +=  "\"sensor{0}\": {1}".format(i, z[i])
                # Set the comma required for true, for the next loop
                comma = True
        # Finish off the Payload JSON
        payload += "}"
        # Publush the sensor data into MQTT
        msg = client.publish(str(data['deviceLocation']) + "/" + str(data['deviceName']), payload)
        # Check to see if the messge was sent, print the error number if there is a problem
        if msg.rc != 0:
            print("Message not sent: " + str(msg.rc))
        # Sleep for a second to allow the system to catch up
        time.sleep(1)
        
except KeyboardInterrupt:
    pass

# Close out all the connections, and stop the loop
ser.close()
client.loop_stop()
client.disconnect()