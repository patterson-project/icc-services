#!/bin/bash
printf "Building and pushing LIGHTING service to dockerhub...\n"
cd ../Service.Lighting && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing UI to dockerhub...\n"
cd Ui && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing BULB controller to dockerhub...\n"
cd Controller.KasaBulb && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing DEVICE service to dockerhub...\n"
cd Service.DeviceManager && bash dockerpush.sh && cd ../

# printf "\nBuilding and pushing LED service to dockerhub...\n"
# cd LedController && bash dockerpush.sh && cd ../


printf "\nDone.\n"
