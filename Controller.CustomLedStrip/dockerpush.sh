#!/bin/bash
sudo docker compose build
sudo docker push $DOCKER_HUB_USERNAME/iot-control-center:led-controller