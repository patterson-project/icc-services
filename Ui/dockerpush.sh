#!/bin/bash
docker-compose build
docker push $DOCKERHUB_USERNAME/iot-control-center:ui
kubectl delete pods -l svc=ui
