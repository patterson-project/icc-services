#!/bin/bash
cd /home/ubuntu/iot-control-center
git pull origin master

cd /home/ubuntu/iot-control-center/BulbController/Bulb1
docker-compose up --build -d