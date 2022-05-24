#!/bin/bash
printf "Building and pushing LIGHTING API service to dockerhub...\n"
cd ../LightingApi && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing UI service to dockerhub...\n"
cd IotControlCenterUi && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing BULB service to dockerhub...\n"
cd BulbController && bash dockerpush.sh && cd ../../

# printf "\nBuilding and pushing LED service to dockerhub...\n"
# cd LedController && bash dockerpush.sh && cd ../


printf "\nDone.\n"
