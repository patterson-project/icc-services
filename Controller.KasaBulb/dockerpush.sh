#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:bulb-controller
kubectl delete pods -l svc=bulb-controller
