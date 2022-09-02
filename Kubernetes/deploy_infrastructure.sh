#!/bin/bash

printf "Deleting all SECRETS...\n"
sudo kubectl delete secret iot-secrets
printf "\nApplying secrets"
envsubst < Secrets/secrets.yaml | sudo kubectl apply -f -


printf "Deleting all SERVICES...\n"
sudo kubectl delete --all services --namespace=default
printf "\n"
for filename in Services/*.yaml; do
    printf "Applying $filename\n"
    envsubst < $filename | sudo kubectl apply -f -
done

printf "\n\nDeleting all INGRESS routing...\n"
sudo kubectl delete --all ingress --namespace=default
printf "\n"
for filename in Ingress/*.yaml; do
    printf "Applying $filename\n"
    envsubst < $filename | sudo kubectl apply -f -
done

printf "\n\nDeleting all DEPLOYMENTS...\n"
sudo kubectl delete --all deployments --namespace=default
printf "\n"
for filename in Deployments/*.yaml; do
    printf "Applying $filename\n"
    envsubst < $filename | sudo kubectl apply -f -
done

printf "\n\nDone.\n"
