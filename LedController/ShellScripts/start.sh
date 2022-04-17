#!/bin/bash
cd /home/pi/led-control-center
git pull origin master

cd /home/pi/led-control-center/LedController
docker-compose up --build -d