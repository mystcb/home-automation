# Home Assistant Setup

Setup for my [Home Assistant](https://home-assistant.io) including all sensor scripts, configuration, and reference material. This readme format has been nicely borrowed from [McAminiti's Git Repo](https://github.com/mcaminiti/homeassistant), with additional help from [basnijholt's setup](https://github.com/basnijholt/home-assistant-config).

# Overview Page

Note this overview page is a work in progress! Having moved house, and finding some amazing new cards, I have been experimenting with them!

![Overview](https://assets.tokonatsu.org.uk/personal/home-assistant/overview-v2.png)

# Devices

## Hubs

| Device                                                                                                                      | Quantity | Connection | Home Assistant                                                              | Notes                                                                           |
| --------------------------------------------------------------------------------------------------------------------------- | :------: | ---------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Phillips Hue Hub v2](https://amzn.to/2WnjUHd)                                                                              |    1     | Ethernet   | [Philips Hue](https://www.home-assistant.io/components/hue/)                | Used to control Phillips Hue Color, Lux, and White bulbs                        |
| [Amazon Echo Dot](https://amzn.to/2WnjUHd)                                                                                  |    5     | Wireless   | [Amazon Alexa](https://www.home-assistant.io/components/alexa/)             | Voice control of the Home Assistant when away from my computer                  |
| [Amazon Echo](https://amzn.to/3r2VAi5)                                                                                      |    2     | Wireless   | [Amazon Alexa](https://www.home-assistant.io/components/alexa/)             | Voice control of the Home Assistant when away from my computer (Larger Version) |
| [dresden elektronik ConBee II](https://amzn.to/3a0vRsj)                                                                     |    1     | USB        | [deCONZ](https://www.home-assistant.io/integrations/deconz/)                | Hub used for IKEA and other devices                                             |
| [Home Assistant SkyConnect](https://www.home-assistant.io/skyconnect/)                                                      |    1     | USB        | [SkyConnect](https://skyconnect.home-assistant.io/)                         | Updated Zigbee/Matter Hub                                                       |
| [Hozelock Cloud Controller Hub](https://www.homebase.co.uk/hozelock-cloud-controller-for-automatic-watering-system_p366624) |    1     | Ethernet   | [RESTful Command](https://www.home-assistant.io/integrations/rest_command/) | Garden Watering                                                                 |

## Lighting

| Device                                                                                                                                                                                                                                      | Quantity | Connection | Home Assistant                                                           | Notes                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: | ---------- | ------------------------------------------------------------------------ | --------------------------------------------- |
| [Philips Hue White and Colour Ambiance](https://amzn.to/2WhoYNq)                                                                                                                                                                            |    5     | Zigbee     | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Colour changing smart bulbs                   |
| [Philips Hue Discover White and Colour Ambiance Led Smart Garden Wall Light](https://amzn.to/2y6xQOJ)                                                                                                                                       |    1     | Zigbee     | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Outdoor lighting                              |
| [TRÅDFRI LED bulb E27 600 lumen, wireless dimmable colour and white spectrum](https://www.ikea.com/gb/en/p/tradfri-led-bulb-e27-600-lumen-wireless-dimmable-colour-and-white-spectrum-colour-and-white-spectrum-globe-opal-white-00408612/) |    3     | Zigbee     | [deCONZ](https://www.home-assistant.io/integrations/deconz/)             | Bedside lamps                                 |
| [TRÅDFRI LED bulb E27 1000 lumen, wireless dimmable white spectrum](https://www.ikea.com/gb/en/p/tradfri-led-bulb-e27-1000-lumen-wireless-dimmable-white-spectrum-white-spectrum-globe-opal-white-60408483/)                                |    3     | Zigbee     | [deCONZ](https://www.home-assistant.io/integrations/deconz/)             | Stand up paper lamps                          |
| [TRÅDFRI LED bulb GU10 400 lumen](https://www.ikea.com/gb/en/p/tradfri-led-bulb-gu10-400-lumen-wireless-dimmable-white-spectrum-90408603/)                                                                                                  |    14    | Zigbee     | [deCONZ](https://www.home-assistant.io/integrations/deconz/)             | Kitchen/Dining Room lights and reading lights |

## Wall Switches

| Device                                                                                                   | Quantity | Connection | Home Assistant                                                           | Notes                                              |
| -------------------------------------------------------------------------------------------------------- | :------: | ---------- | ------------------------------------------------------------------------ | -------------------------------------------------- |
| [Philips Hue Smart Wireless Dimmer Switch](https://amzn.to/34rjJzD)                                      |    7     | Zigbee     | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Switched around the house                          |
| [TRÅDFRI Wireless dimmer (Square)](https://www.ikea.com/gb/en/p/tradfri-wireless-dimmer-white-00468432/) |    4     | Zigbee     | [deCONZ](https://www.home-assistant.io/integrations/deconz/)             | Light switch for the loft lights                   |
| [TRÅDFRI Remote control (Round)](https://www.ikea.com/gb/en/p/tradfri-remote-control-30443124/)          |    4     | Zigbee     | [deCONZ](https://www.home-assistant.io/integrations/deconz/)             | Light switch for uplight, kitchen and dining rooms |

## Climate

| Device                                                                                                                            | Quantity | Connection | Home Assistant                                                                                | Notes                                                          |
| --------------------------------------------------------------------------------------------------------------------------------- | :------: | ---------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [BME680 Breakout - Air Quality, Temerature, Pressure, Humidity Sensor](https://thepihut.com/products/bme680?variant=696828526609) |    3     | Wireless   | Sensor attached to a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w) |
| [Hive Active Heating Thermostat](https://amzn.to/2JT5D0i)                                                                         |    2     | Wireless   | [Hive](https://www.home-assistant.io/integrations/hive/)                                      | Manually installed                                             |
| [Hive TRV](https://amzn.to/2Xqhx9R)                                                                                               |    10    | Wireless   | [Hive](https://www.home-assistant.io/integrations/hive/)                                      | Had to add [Magnets](https://amzn.to/2RwnJJL) to make it work! |

## Security

| Device                                                                                                                     | Quantity | Connection | Home Assistant                                                                                                   | Notes                  |
| -------------------------------------------------------------------------------------------------------------------------- | :------: | ---------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [Alarm Reed Switch - HAA27](https://cpc.farnell.com/unbranded/haa27/switch-reed-alarm/dp/SR06273)                          |    5     | Wireless   | Sensor attached to a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w) (No longer in use) |
| [TRÅDFRI Wireless motion sensor](https://www.ikea.com/gb/en/p/tradfri-wireless-motion-sensor-white-70429913/)              |    4     | Wireless   | [deCONZ](https://www.home-assistant.io/integrations/deconz/)                                                     | Set to 1 minute timers |
| [Hive Pet Friendly Motion Sensors ](https://www.hivehome.com/shop/smart-sensors-and-plugs/hive-pet-friendly-motion-sensor) |    5     | Wireless   | [SkyConnect](https://skyconnect.home-assistant.io/)                                                              | Motion LED's enabled   |

## Media

| Device                               | Quantity | Connection | Home Assistant                                                                                                                                      | Notes        |
| ------------------------------------ | :------: | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [Plex Media Server](https://plex.tv) |    1     | Ethernet   | [Plex](https://www.home-assistant.io/components/media_player.plex) / [Plex Activity Monitor](https://www.home-assistant.io/components/sensor.plex/) | Media Server |

## Motion Sensors

| Device                                                       | Quantity | Connection | Home Assistant                                                           | Notes                                                   |
| ------------------------------------------------------------ | :------: | ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------- |
| [Philips Hue Outdoor Motion Sensor](https://amzn.to/2JTEhHx) |    2     | Zigbee     | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Trigger the outdoor lights, and for temperature sensing |

## Power Switches / Monitoring

| Device                                                                                                                                                 |  Quantity  | Connection | Home Assistant                                                           | Notes                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------: | ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| [TRÅDFRI Wireless control outlet](https://www.ikea.com/gb/en/p/tradfri-wireless-control-outlet-00364477/)                                              |     12     | Zigbee     | [deCONZ](https://www.home-assistant.io/integrations/deconz/)             | Controls multiple lamps and devices                           |
| [TP-Link Kasa Smart Plug HS110](https://amzn.to/2xlbJUA)                                                                                               |     6      | Wireless   | [TP-Link Kasa Smart](https://www.home-assistant.io/integrations/tplink/) | Also monitors power usage (no longer in use)                  |
| [Local Bytes Smart Plug](https://www.mylocalbytes.com/products/smart-plug-pm)                                                                          |     4      | Wireless   | [Tasmota](https://www.home-assistant.io/integrations/tasmota)            | Also monitors power usage (new version)                       |
| [Power HAT (RPICT3V1) for Raspberry Pi](https://lechacalshop.com/gb/rpict-series/20-1550-raspberrypi-1x-current-sensor-adaptor-1-voltage-emoncms.html) | 1 + 1 Clip | Wireless   | [MQTT](https://www.home-assistant.io/integrations/mqtt/)                 | Clip on sensor to monitor power usage, requires power adaptor |

## Network

| Device                                                                         | Quantity | Connection | Home Assistant                                                                       | Notes                                                                        |
| ------------------------------------------------------------------------------ | :------: | ---------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| [Ubiquiti Networks Unifi Security Gateway (USG)](https://amzn.to/2GTuoYh)      |    1     | Ethernet   | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/) | Primary Router. Presence detection for devices                               |
| [Ubiquiti Networks UniFi Switch - 8 Ports (US-8-60W)](https://amzn.to/2LllvMN) |    2     | Ethernet   | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/) | Primary Switch. Presence detection devices                                   |
| [Ubiquiti UniFi AC Outdoor Mesh (UAP-AC-M-PRO)](https://amzn.to/2VFp7x6)       |    1     | Ethernet   | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/) | Wireless Access Point for interior coverage. Presence detection for devices. |
| [Ubiquiti UniFi 6 Pro Acces Point Wifi 6 AP (U6-PRO)](https://amzn.to/3Xt3Sfp) |    2     | Ethernet   | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/) | Wireless Access Point for interior coverage. Presence detection for devices. |

## Hardware

| Device                                                                                                                                                                                         | Quantity | Connection | Home Assistant                                                               | Notes                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: | ---------- | ---------------------------------------------------------------------------- | ------------------------------------ |
| [Raspberry Pi Zero W](https://thepihut.com/collections/raspberry-pi/products/raspberry-pi-zero-w)                                                                                              |    5     | Wireless   | N/A                                                                          | Base for the DIY sensors             |
| [Raspberry Pi Zero v1.3](https://thepihut.com/collections/raspberry-pi/products/raspberry-pi-zero)                                                                                             |    4     | USB WiFi   | N/A                                                                          | Base for the DIY sensors             |
| [Raspberry Pi NoIR Camera V2](https://www.raspberrypi.org/products/pi-noir-camera-v2/)                                                                                                         |    1     | N/A        | [motionEye Add-On](https://github.com/hassio-addons/addon-motioneye)         | Night vision camera                  |
| [Raspberry Pi Camera V2](https://thepihut.com/collections/raspberry-pi-camera/products/raspberry-pi-camera-module)                                                                             |    1     | N/A        | [motionEye Add-On](https://github.com/hassio-addons/addon-motioneye)         | HD Camera                            |
| [Intel NUC i7](https://www.intel.com/content/www/us/en/products/boards-kits/nuc/kits/nuc5i7ryh.html)                                                                                           |    1     | Ethernet   | Yes!                                                                         | Upgrade from an older RPi2           |
| [Amazon Kindke Fire 7" 2015](https://uk.webuy.com/product-detail?id=samasv98ln05b&categoryName=tablets-android&superCatName=computing&title=amazon-kindle-fire-8gb-7%22-2015-5th-generation-b) |    2     | Wireless   | [MQTT Alarm Panel](https://github.com/thanksmister/android-mqtt-alarm-panel) | Alarm panels and Appdaemon Dashboard |

## Software

| Device                              | Quantity | Connection | Home Assistant                                                             | Notes                                                                                                                                                                                                                           |
| ----------------------------------- | :------: | ---------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Pi-hole](https://pi-hole.net)      |    2     | Ethernet   | [Pi-Hole Sensor](https://www.home-assistant.io/components/sensor.pi_hole/) | Ad blocking. Instance runs within a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w)                                                                                                                    |
| [LineageOS](https://lineageos.org/) |    2     | N/A        | N/A                                                                        | Replacement Android Software for [Amazon Kindke Fire 7" 2015](https://uk.webuy.com/product-detail?id=samasv98ln05b&categoryName=tablets-android&superCatName=computing&title=amazon-kindle-fire-8gb-7%22-2015-5th-generation-b) |

## Loft Antenna Device

| Device                                                                                                                                                                                    | Quantity | Connection | Home Assistant                                           | Notes                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: | ---------- | -------------------------------------------------------- | --------------------------------------------- |
| [FlightAware Pro Stick Plus (USB SDR ADS-B Receiver](https://thepihut.com/products/flightaware-pro-stick-plus-usb-sdr-ads-b-receiver)                                                     |    1     | USB        | [MQTT](https://www.home-assistant.io/integrations/mqtt/) | Main USB scanning device for aeroplanes       |
| [60cm 1090MHz Antenna for ADS-B](https://thepihut.com/products/60cm-1090mhz-antenna-for-ads-b)                                                                                            |    1     | Cable      | [MQTT](https://www.home-assistant.io/integrations/mqtt/) | Larger antenna for the ADS-B Receiver         |
| [Adafruit Ultimate GPS HAT for Raspberry Pi A+/B+/Pi 2/3/Pi 4 (Mini Kit)](https://thepihut.com/products/adafruit-ultimate-gps-hat-for-raspberry-pi-a-b-pi-2-mini-kit?variant=27739829777) |    1     | Header     | N/A                                                      | GPS Receiver to create a Stratum 0 NTP server |

## Other Items / Misc.

| Device                                                  | Quantity | Connection | Home Assistant                                           | Notes                                         |
| ------------------------------------------------------- | :------: | ---------- | -------------------------------------------------------- | --------------------------------------------- |
| [Elegoo 4 Channel Relay Board](https://amzn.to/2Kmcr6W) |    1     | Wireless   | [MQTT](https://www.home-assistant.io/integrations/mqtt/) | Relay trigger for Doorbell (no longer in use) |
