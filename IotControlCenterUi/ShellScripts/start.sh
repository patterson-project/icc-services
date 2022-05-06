#!/bin/bash
cd /home/ubuntu/iot-control-center
git pull origin master

cd /home/ubuntu/iot-control-center/IotControlCenterUi
docker-compose up --build -d