#!/bin/bash
sudo docker compose build
sudo docker push $DOCKERHUB_USERNAME/iot-control-center:ui
sudo kubectl delete pods -l svc=ui
