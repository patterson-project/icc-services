#!/bin/bash
cd /home/pi/led-control-center
git pull origin master

cd /home/pi/led-control-center/BulbController
docker-compose up --build -d