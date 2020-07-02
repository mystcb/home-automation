# MicroPython Bootstraping

To ensure that all ESP8266 devices have the same modules, this directory ensures that the same files are available, and also kept up to date. The bootstrap requires a few commands to be available. These are the ones used are for my macOS laptop.

For this project, I have been using a WeMos D1 Mini

## Requirements
* [CH340 Driver for the WeMos](https://docs.wemos.cc/en/latest/ch340_driver.html)
* ESPTool - either `pip install esptool` or `brew install esptool`
* [The MicroPython Kernel](https://micropython.org/download#esp8266)
* Adafruit MicroPython tool aka `ampy` - `pip install adafruit-ampy`
* picocom - `brew install picocom`

## Setting up the WeMos
1. Find the USB Serial Interface for the D1 Mini, for me it was `/dev/tty.wchusbserial310`
2. Erase the flash on the ESP8266 controller

    `esptool.py --port PORT_NAME erase_flash`

3. Load the firmware to the ESP8266 controller

    `esptool.py --port PORT_NAME --baud 1000000 write_flash --flash_size=4MB -fm dio 0 FIRMWARE.bin`

4. Using picocom, connect ensure it is working

    `picocom /dev/tty.wchusbserial310 -b115200`
    
    You should then receive the following prompt:

    ```
       MicroPython v1.12 on 2019-12-20; ESP module with ESP8266
       Type "help()" for more information.
       >>>
    ```

5. Disable OS Debug so that `ampy` can connect

   ``` python
   import esp
   esp.osdebug(None)
   ```

6. Check you can connect to the ESP8266 with ampy

   `ampy -d 0.5 --port /dev/tty.wchusbserial310 --baud 115200 ls`

   * `-d 0.5` has been added as a delay, due to an issue with the CH340 driver on macOS

## Bootstrap loading
Running the script `boostrap_load.sh` will ensure all of the python files and modules from this folder are copied to the correct locations on the devices.
 
`bootstrap_load.sh /dev/tty.wchusbserial310`


## The bootstrapped files

* `boot.py` - An updated boot file which disables the osdebug on each boot
* `mqtt.py` - An MQTT micro module to allow the ESP8266 to publish to ah MQTT queue.
* `common.py` - A bunch of common functions for use with the ESP8266 