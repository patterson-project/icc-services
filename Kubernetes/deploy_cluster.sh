#!/bin/bash
printf "Building and pushing LIGHTING service to dockerhub...\n"
cd ../Service.Lighting && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing DEVICE MANAGER service to dockerhub...\n"
cd Service.DeviceManager && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing UI to dockerhub...\n"
cd Ui && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing KASA BULB controller to dockerhub...\n"
cd Controller.KasaBulb && bash dockerpush.sh && cd ../

printf "\nBuilding and pushing KASA LED STRIP service to dockerhub...\n"
cd Controller.KasaLedStrip && bash dockerpush.sh && cd ../

printf "\nDone.\n"
