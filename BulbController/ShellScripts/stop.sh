#!/bin/bash
cd /home/pi/iot-control-center
git pull origin master

cd /home/pi/iot-control-center/LedController
docker-compose up --build -d