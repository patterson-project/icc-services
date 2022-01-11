#!/bin/bash
cd /home/ubuntu/led-control-center
git pull origin master

cd /home/ubuntu/led-control-center/LedApi
docker-compose up --build -d