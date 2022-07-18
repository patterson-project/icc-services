#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:device-manager-service
kubectl delete pods -l svc=device-manager-service
