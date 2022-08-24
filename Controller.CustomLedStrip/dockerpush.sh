#!/bin/bash
docker-compose build
docker push $DOCKERHUB_USERNAME/iot-control-center:led-controller