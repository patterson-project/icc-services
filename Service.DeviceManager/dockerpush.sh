#!/bin/bash
sudo docker compose build
sudo docker push $DOCKERHUB_USERNAME/iot-control-center:device-manager-service
sudo kubectl delete pods -l svc=device-manager-service
