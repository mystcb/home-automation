# Home Assistant Setup

Setup for my [Home Assistant](https://home-assistant.io) including all sensor scripts, configuration, and reference material. This readme format has been nicely borrowed from [McAminiti's Git Repo](https://github.com/mcaminiti/homeassistant).

# Devices

## Hubs

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Phillips Hue Hub v2](https://amzn.to/2WnjUHd) | 1 | Ethernet | [Philips Hue](https://www.home-assistant.io/components/hue/) | Used to control Phillips Hue Color, Lux, and White bulbs |
| [Amazon Echo Dot](https://amzn.to/2WnjUHd) | 1 | Wireless | [Amazon Alexa](https://www.home-assistant.io/components/alexa/) | Voice control of the Home Assistant when away from my computer |

## Lighting

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Philips Hue White and Colour Ambiance](https://amzn.to/2WhoYNq) | 3 | Ethernet | [Philips Hue Light](https://www.home-assistant.io/components/light.hue/) | Colour changing smart bulbs|

## Climate

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [BME680 Breakout - Air Quality, Temerature, Pressure, Humidity Sensor](https://thepihut.com/products/bme680?variant=696828526609) | 2 | Wireless | Sensor attached to a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w) |

## Security

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Alarm Reed Switch - HAA27](https://cpc.farnell.com/unbranded/haa27/switch-reed-alarm/dp/SR06273) | 5 | Wireless | Sensor attached to a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w) |

## Media

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |
| [Plex Media Server](https://plex.tv) | 1 | Ethernet | [Plex](https://www.home-assistant.io/components/media_player.plex) / [Plex Activity Monitor](https://www.home-assistant.io/components/sensor.plex/) |  Media Server|  

## Sensors

| Device  | Quantity | Connection | Home Assistant | Notes |
| ------------- | :---: | ------------- | ------------- | ------------- |

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