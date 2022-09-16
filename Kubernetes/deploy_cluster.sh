#!/bin/bash

# Colors
cyn=$'\e[1;36m'
grn=$'\e[1;32m'
end=$'\e[0m'

printf "%s\n" "${cyn}Building and pushing LIGHTING service to dockerhub...${end}"
cd ../Service.Lighting && bash dockerpush.sh && cd ../

printf "\n%s\n" "${cyn}Building and pushing DEVICE MANAGER service to dockerhub...${end}"
cd Service.DeviceManager && bash dockerpush.sh && cd ../

printf "\n%s\n" "${cyn}Building and pushing UI to dockerhub...${end}"
cd Ui && bash dockerpush.sh && cd ../

printf "\n%s\n" "${cyn}Building and pushing KASA BULB controller to dockerhub...${end}"
cd Controller.KasaBulb && bash dockerpush.sh && cd ../

printf "\n%s\n" "${cyn}Building and pushing KASA LED STRIP service to dockerhub...${end}"
cd Controller.KasaLedStrip && bash dockerpush.sh && cd ../

printf "\n%s\n" "${grn}Done.${end}"
