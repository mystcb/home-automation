# Created by Colin Barker (colin@faereal.net)
# main.py - ESP8266 Entrypoint file
#

# Modules to import
import common # pylint: disable=import-error
import machine  # pylint: disable=import-error
import time

# Setup the reset pin to D6
breakPin = machine.Pin(12, machine.Pin.IN)
if (breakPin.value() == 1):
    # Break pin isn't grounded, so continue with the loop!
    print("Running main program")

    # Read the configuration file
    print("reading config")
    config = common.read_config("config.json")

    # Enable the moisture sensor on pin D8
    print("enabling sensor")
    moisturePowerPin = machine.Pin(15, machine.Pin.OUT).on()
    time.sleep(1)

    # Read the sensor value
    print("reading sensor")
    value = machine.ADC(0).read()

    # Disable the moisture sensor power
    print("disabling sensor")
    moisturePowerPin = machine.Pin(15, machine.Pin.OUT).off()

    # Connect to the WiFi
    print("connecting to WiFI")
    sta_if = common.wifi_connect(config["wifiEssid"], config["wifiPassword"])

    # Push message to MQTT
    print("publishing value to MQTT")
    common.mqtt_publish(str(config["clientId"]), str(config["mqttHost"]), str(config["mqttUsername"]), str(config["mqttPassword"]), 1883, str(config["deviceLocation"] + "/" + config['deviceName'] + "/moisture"), str(value))
    time.sleep(1)

    # Disable WiFi
    print("disconnecting from WiFi")
    sta_if.disconnect()

    # Enable Deep Sleep Mode
    print("enabling deep sleep mode")
    common.deep_sleep(10000)


## Only get here if the break has been it
print("Break in loop, falling back to prompt")