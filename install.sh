#!/bin/bash

# Uncomment if first time installing
# curl -fsSL https://get.docker.com -o get-docker.sh
# sh get-docker.sh
# apt install docker-compose -y

cd IotControlCenterUi/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh
cd ../../

cd Api/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh
cd ../../

cd LedController/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh
cd ../../

cd LedController/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh
cd ../../

cd LedController/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh
cd ../../

cp SystemdFiles/* /etc/systemd/system/

