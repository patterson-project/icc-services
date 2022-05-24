#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:lighting-api
k delete pods -l svc=lighting-api