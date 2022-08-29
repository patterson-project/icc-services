#!/bin/bash
sudo docker compose build
docker push $DOCKERHUB_USERNAME/iot-control-center:kasa-led-strip-controller
sudo kubectl delete pods -l svc=kasa-led-strip-controller
