
##
# Connect to the WiFi
# return: station interface
##
def wifi_connect(essid, password):
    import network # pylint: disable=import-error

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    return sta_if

##
# Write message to MQTT
##
# Callback function
def mqtt_callback(topic, msg):
    print(msg)

# Main function
def mqtt_publish(device, host, username, pwd, cport, mqtt_topic, mqtt_message):
    from mqtt import MQTTClient # pylint: disable=import-error

    client = MQTTClient(device,host,user=username,password=pwd,port=cport)
    client.set_callback(mqtt_callback)
    client.connect()
    client.publish(topic=mqtt_topic,msg=mqtt_message)
    #client.disconnect()
    print('message sent')


##
# Read a configuration file
##
def read_config(filename):
    import json
    import sys

    try:
        with open(str(filename)) as config_file:
            return json.load(config_file)
    except Exception as e:
        print("Error with configuration file: " + str(e))
        sys.exit(1)

##
# Deep Sleep ESP8266
##
def deep_sleep(ms=10000):
    import machine # pylint: disable=import-error

    # Configure the RTC and ALARM0 to wake the ESP8266
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    # Set the alarm to trigger after x number milliseconds
    rtc.alarm(rtc.ALARM0, ms)

    # Put the ESP8266 into deepsleep
    machine.deepsleep()