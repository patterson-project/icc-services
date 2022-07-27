#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:lighting-service
kubectl delete pods -l svc=lighting-service
