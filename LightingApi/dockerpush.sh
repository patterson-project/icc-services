#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:lighting-api
microk8s kubectl delete pods -l svc=lighting-api