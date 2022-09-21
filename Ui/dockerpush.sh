#!/bin/bash
sudo docker compose build
sudo docker push $DOCKER_HUB_USERNAME/iot-control-center:ui
sudo kubectl delete pods --wait=false -l svc=ui
