#!/usr/bin/python3
# MQTT Publish Script for Home Sensors - Power
# -----------------------------------------------
# by Colin Barker (colin@faereal.net)
#
# Connets to an MQTT server and publishes data collected by
# a Raspberry Pi, connected to a SolarMax 2000S inverter, though
# a crossover ethernet cable.

# Import all the modules required
import json, time, sys
import paho.mqtt.client as mqtt
import argparse
from solarmax3 import SolarMax

# Setup arguments for use with the CLI
parser = argparse.ArgumentParser()
parser.add_argument(
    '-C', 
    '--config', 
    required=True, 
    default=str("config.json"), 
    help="location of the config file (json)", 
    metavar="file"
    )

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


# Set up the configuration for the inverters
inverters = data['inverterList']

smlist = []
allinverters = []
for host in inverters.keys():
    sm = SolarMax(host, 12345)
    sm.use_inverters(inverters[host])
    smlist.append(sm)
    allinverters.extend(inverters[host])

# Start the loop
client.loop_start()

# Main monitoring loop
try:
    while True:
        # Initialise a counter to 0
        count = 0
        # Loop over all the inverters
        for sm in smlist:
            for (no, ivdata) in sm.inverters().items():
                try:
                    # Get the latest info
                    (inverter, current) = sm.query(no, ['PAC', 'KDY', 'KT0', 'IDC', 'UDC', 'IL1', 'UL1', 'FDAT', 'SYS'])
                    current_value = current['PAC']
                    count += 1
                except: # pylint: disable=bare-except
                    print(f'Communication Error, WR {no}')
                    # Set the current to 0 to ensure a good reading
                    current_value = 0

                # So we have the data, lets check the status first
                (status, errors) = sm.status(no)
                # Initial part of the Payload JSON
                payload = f'''{{
        \"sensor{no}\": {{
            \"current\": {current_value},
            \"status\": "{status}",
            \"errors\": "{errors}"
        }}
    }}
    '''
                # Publish the sensor data into MQTT
                msg = client.publish(str(data['deviceLocation']) + "/" + str(data['deviceName']), payload)
                # Check to see if the message was sent, print the error number if there is a problem
                if msg.rc != 0:
                    print("Message not sent: " + str(msg.rc))
        
        # Lets check the number of messages sent (likely 0 if the inverter is off)
        if count < len(allinverters):
            for inverter in allinverters:
                payload = f'''{{
        \"sensor{inverter}\": {{ 
            \"current\": 0,
            \"status\": "Offline",
            \"errors\": "Too little irradiation"
                    }}
    }}
    '''
                # Publish the sensor data into MQTT
                msg = client.publish(str(data['deviceLocation']) + "/" + str(data['deviceName']), payload)
                # Check to see if the message was sent, print the error number if there is a problem
                if msg.rc != 0:
                    print("Message not sent: " + str(msg.rc))

                # Set a longer sleep time
                time.sleep(59)

        # Sleep for a second to allow the system to catch up
        time.sleep(1)

except KeyboardInterrupt:
    pass

# # Close out all the connections, and stop the loop
client.loop_stop()
client.disconnect()
