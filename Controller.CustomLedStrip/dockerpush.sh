#!/bin/bash
sudo docker compose build
sudo docker push $DOCKERHUB_USERNAME/iot-control-center:led-controller