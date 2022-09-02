#!/bin/bash

# Installing docker and docker compose
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Logging user into dockerhub
sudo docker login

# Installing Kubernetes
curl -sfL https://get.k3s.io | sh -
# sudo apt install -y linux-modules-extra-raspi
# sudo sed -i '$s/$/ cgroup_memory=1 cgroup_enable=memory/' /boot/cmdline.txt 

echo "namespace 8.8.8.8" >> /etc/resolv.conf
echo "namespace 8.8.4.4" >> /etc/resolv.conf

# Setting up environment variables
echo "Environment variable setup"
read -p "Choose a database username: " mongo_username
read -p "Choose a database password: " mongo_password
read -p "Enter the IP of your device: " mongo_ip
read -p "Enter your dockerhub username: " dockerhub_username

echo "MONGO_DB_USERNAME=$mongo_username" >> /etc/environment
echo "MONGO_DB_PASSWORD=$mongo_password" >> /etc/environment
echo "MONGO_DB_IP=$mongo_ip" >> /etc/environment
echo "DOCKERHUB_USERNAME=$dockerhub_username" >> /etc/environment

source /etc/environment

# Deploying the MongoDb locally
cd MongoDb
sudo docker compose up --build -d

# Deploying cluster infrastructure
cd Kubernetes
sudo bash deploy_infrastructure.sh

# Building and deploying cluster
sudo bash deploy_cluster.sh

# Restarting for changes to take effect
sudo reboot