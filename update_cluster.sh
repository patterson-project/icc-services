#!/bin/bash
printf "Building and pushing API service to dockerhub..."
cd Api && sh dockerpush.sh && cd ../
printf "\nBuilding and pushing UI service to dockerhub..."
cd IotControlCenterUi && sh dockerpush.sh && cd ../
printf "\nBuilding and pushing BULB 1 service to dockerhub..."
cd BulbController/Bulb1 && sh dockerpush.sh && cd ../../
printf "\nBuilding and pushing BULB 2 service to dockerhub..."
cd BulbController/Bulb2 && sh dockerpush.sh && cd ../../
printf "\nBuilding and pushing LED service to dockerhub..."
cd LedController && sh dockerpush.sh && cd ../

printf "\n\nDeleting and restarting all pods..."
microk8s kubectl delete --all pods --namespace=default

printf "\nDone.\n"
