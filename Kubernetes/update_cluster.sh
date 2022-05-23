#!/bin/bash
printf "Building and pushing DATABASE service to dockerhub...\n"
cd ../DeviceDatabase && bash dockerpush.sh && cd ../

printf "Building and pushing LIGHTING API service to dockerhub...\n"
cd ../LightingApi && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing UI service to dockerhub...\n"
cd IotControlCenterUi && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing BULB service to dockerhub...\n"
cd BulbController && bash dockerpush.sh && cd ../../

# printf "\nBuilding and pushing LED service to dockerhub...\n"
# cd LedController && bash dockerpush.sh && cd ../

printf "\nDeleting and restarting all pods...\n"
microk8s kubectl delete --all pods --namespace=default

printf "\nDone.\n"
