#!/bin/bash
docker-compose build
docker push $DOCKERHUB_USERNAME/iot-control-center:device-manager-service
kubectl delete pods -l svc=device-manager-service
