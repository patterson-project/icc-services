#!/bin/bash
cd /home/ubuntu/iot-control-center
git pull origin master

cd /home/ubuntu/iot-control-center/Api
docker-compose up --build -d
