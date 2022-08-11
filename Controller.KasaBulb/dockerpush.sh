#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:kasa-bulb-controller
kubectl delete pods -l svc=kasa-bulb-controller
