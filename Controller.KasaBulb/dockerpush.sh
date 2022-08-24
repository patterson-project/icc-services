#!/bin/bash
docker-compose build
docker push $DOCKERHUB_USERNAME/iot-control-center:kasa-bulb-controller
kubectl delete pods -l svc=kasa-bulb-controller
