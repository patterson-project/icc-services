#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:ui
kubectl delete pods -l svc=ui
