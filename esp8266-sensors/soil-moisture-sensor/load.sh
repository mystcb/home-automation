#!/bin/bash
if [ -z "$1" ]; then
    echo "You have not selected a port"
    exit 1;
fi

echo "Copying files (takes some time!)"
ampy -d 0.5 --port $1 --baud 115200 put config.json config.json
ampy -d 0.5 --port $1 --baud 115200 put main.py main.py

echo "Resetting device"
ampy -d 0.5 --port $1 --baud 115200 reset