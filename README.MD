# Home Assistant Setup

Setup for my [Home Assistant](https://home-assistant.io) including all sensor scripts, configuration, and reference material. This readme format has been nicely borrowed from [McAminiti's Git Repo](https://github.com/mcaminiti/homeassistant), with additional help from [basnijholt's setup](https://github.com/basnijholt/home-assistant-config).

# Overview Page
![Overview](https://assets.tokonatsu.org.uk/personal/home-assistant/overview.png)

# Devices

## Hubs

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Phillips Hue Hub v2](https://amzn.to/2WnjUHd) | 1 | Ethernet | [Philips Hue](https://www.home-assistant.io/components/hue/) | Used to control Phillips Hue Color, Lux, and White bulbs |
| [Amazon Echo Dot](https://amzn.to/2WnjUHd) | 1 | Wireless | [Amazon Alexa](https://www.home-assistant.io/components/alexa/) | Voice control of the Home Assistant when away from my computer |
| [dresden elektronik ConBee II](https://amzn.to/3a0vRsj) | 1 | USB | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | Hub used for IKEA and other devices |

## Lighting

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Philips Hue White and Colour Ambiance](https://amzn.to/2WhoYNq) | 5 | Zigbee | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Colour changing smart bulbs|
| [Philips Hue Discover White and Colour Ambiance Led Smart Garden Wall Light](https://amzn.to/2y6xQOJ) | 1 | Zigbee | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Outdoor lighting |
| [TRÅDFRI LED bulb E27 600 lumen, wireless dimmable colour and white spectrum](https://www.ikea.com/gb/en/p/tradfri-led-bulb-e27-600-lumen-wireless-dimmable-colour-and-white-spectrum-colour-and-white-spectrum-globe-opal-white-00408612/) | 1 | Zigbee | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | |
| [TRÅDFRI LED bulb E27 1000 lumen, wireless dimmable white spectrum](https://www.ikea.com/gb/en/p/tradfri-led-bulb-e27-1000-lumen-wireless-dimmable-white-spectrum-white-spectrum-globe-opal-white-60408483/) | 3 | Zigbee | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | Stand up paper lamps |
| [TRÅDFRI LED bulb GU10 400 lumen](https://www.ikea.com/gb/en/p/tradfri-led-bulb-gu10-400-lumen-wireless-dimmable-white-spectrum-90408603/) | 1 | Zigbee | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | Reading light |

## Wall Switches
| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Philips Hue Smart Wireless Dimmer Switch](https://amzn.to/34rjJzD) | 7 | Zigbee | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Switched around the house |
| [TRÅDFRI Wireless dimmer (Square)](https://www.ikea.com/gb/en/p/tradfri-wireless-dimmer-white-00468432/) | 1 | Zigbee | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | Light switch for the loft lights |
| [TRÅDFRI Remote control (Round)](https://www.ikea.com/gb/en/p/tradfri-remote-control-30443124/) | 1 | Zigbee | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | Light switch for uplight |

## Climate

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [BME680 Breakout - Air Quality, Temerature, Pressure, Humidity Sensor](https://thepihut.com/products/bme680?variant=696828526609) | 2 | Wireless | Sensor attached to a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w) |
| [Hive Active Heating Thermostat](https://amzn.to/2JT5D0i) | 1 | Wireless | [Hive](https://www.home-assistant.io/integrations/hive/) | Manually installed |
| [Hive TRV](https://amzn.to/2Xqhx9R) | 6 | Wireless | [Hive](https://www.home-assistant.io/integrations/hive/) | Had to add [Magnets](https://amzn.to/2RwnJJL) to make it work! |

## Security

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Alarm Reed Switch - HAA27](https://cpc.farnell.com/unbranded/haa27/switch-reed-alarm/dp/SR06273) | 5 | Wireless | Sensor attached to a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w) |
| [TRÅDFRI Wireless motion sensor](https://www.ikea.com/gb/en/p/tradfri-wireless-motion-sensor-white-70429913/) | 3 | Wireless | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | Set to 1 minute timers |

## Media

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Plex Media Server](https://plex.tv) | 1 | Ethernet | [Plex](https://www.home-assistant.io/components/media_player.plex) / [Plex Activity Monitor](https://www.home-assistant.io/components/sensor.plex/) |  Media Server |  

## Sensors

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Philips Hue Outdoor Motion Sensor](https://amzn.to/2JTEhHx) | 1 | Zigbee | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Trigger the outdoor lights |

## Power Switches

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [TRÅDFRI Wireless control outlet](https://www.ikea.com/gb/en/p/tradfri-wireless-control-outlet-00364477/) | 6 | Zigbee | [deCONZ](https://www.home-assistant.io/integrations/deconz/) | Controls multiple lamps and devices
| [TP-Link Kasa Smart Plug HS110](https://amzn.to/2xlbJUA) | 4 | Wireless | [TP-Link Kasa Smart](https://www.home-assistant.io/integrations/tplink/) | Also monitors power usage |

## Network

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Ubiquiti Networks Unifi Security Gateway (USG)](https://amzn.to/2GTuoYh) | 1 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Primary Router. Presence detection for devices |
| [Ubiquiti Networks UniFi Switch - 8 Ports (US-8-60W)](https://amzn.to/2LllvMN) | 2 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Primary Switch. Presence detection devices |
| [Ubiquiti UniFi AC Outdoor Mesh (UAP-AC-M-PRO)](https://amzn.to/2VFp7x6) | 2 | Ethernet | [Ubiquiti Unifi WAP](https://www.home-assistant.io/components/device_tracker.unifi/)| Wireless Access Point for interior coverage. Presence detection for devices. |

## Software

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Pi-hole](https://pi-hole.net) | 2 | Ethernet | [Pi-Hole Sensor](https://www.home-assistant.io/components/sensor.pi_hole/) | Ad blocking. Instance runs within a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w) |