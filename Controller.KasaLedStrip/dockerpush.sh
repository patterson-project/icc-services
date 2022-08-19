#!/bin/bash
docker-compose build
docker push canadrian72/iot-control-center:kasa-led-strip-controller
kubectl delete pods -l svc=kasa-led-strip-controller
