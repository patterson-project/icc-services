#!/bin/bash
docker-compose build
docker push $DOCKERHUB_USERNAME/iot-control-center:lighting-service
kubectl delete pods -l svc=lighting-service
