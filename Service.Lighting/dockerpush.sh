#!/bin/bash
sudo docker compose build
docker push $DOCKERHUB_USERNAME/iot-control-center:lighting-service
sudo kubectl delete pods -l svc=lighting-service
