#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:ui
microk8s kubectl delete pods -l svc=ui