#!/bin/bash
printf "Building and pushing API service to dockerhub...\n"
cd Api && sh dockerpush.sh && cd ../
printf "\nBuilding and pushing UI service to dockerhub...\n"
cd IotControlCenterUi && sh dockerpush.sh && cd ../
printf "\nBuilding and pushing BULB 1 service to dockerhub...\n"
cd BulbController/Bulb1 && sh dockerpush.sh && cd ../../
printf "\nBuilding and pushing BULB 2 service to dockerhub...\n"
cd BulbController/Bulb2 && sh dockerpush.sh && cd ../../
printf "\nBuilding and pushing LED service to dockerhub...\n"
cd LedController && sh dockerpush.sh && cd ../

printf "\nDeleting and restarting all pods...\n"
microk8s kubectl delete --all pods --namespace=default

printf "\nDone.\n"
