#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:bulb-controller
microk8s kubectl delete pods -l svc=bulb-controller
