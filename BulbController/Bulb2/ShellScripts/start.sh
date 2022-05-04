#!/bin/bash
cd /home/pi/iot-control-center
git pull origin master

cd /home/pi/iot-control-center/BulbController/Bulb2
docker-compose up --build -d