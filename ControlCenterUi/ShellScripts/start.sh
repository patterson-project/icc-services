#!/bin/bash
cd /home/ubuntu/iot-control-center
git pull origin master

cd /home/ubuntu/iot-control-center/ControlCenterUi
docker-compose up --build -d