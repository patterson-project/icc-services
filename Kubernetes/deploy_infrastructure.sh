#!/bin/bash

# Colors
cyn=$'\e[1;36m'
grn=$'\e[1;32m'
end=$'\e[0m'

printf "%s\n" "${cyn}Deploying all SECRETS...${end}"
sudo kubectl delete secret iot-secrets --wait=false
envsubst < Secrets/secrets.yaml | sudo kubectl apply -f -


printf "\n%s\n" "${cyn}Deploying all SERVICES...${end}"
sudo kubectl delete --all services --wait=false --namespace=default
for filename in Services/*.yaml; do
    printf "%s\n" "Applying $filename"
    envsubst < $filename | sudo kubectl apply -f -
done

printf "\n%s\n" "${cyn}Deploying all INGRESS routing...${end}"
sudo kubectl delete --all ingress --wait=false --namespace=default
for filename in Ingress/*.yaml; do
    printf "%s\n" "Applying $filename"
    envsubst < $filename | sudo kubectl apply -f -
done

printf "\n%s\n" "${cyn}Deploying all DEPLOYMENTS...${end}"
sudo kubectl delete --all deployments --wait=false --namespace=default
for filename in Deployments/*.yaml; do
    printf "Applying $filename\n"
    envsubst < $filename | sudo kubectl apply -f -
done

printf "\n%\n" "${grn}Done.${end}"
