#!/bin/bash
printf "Deleting all SERVICES...\n"
microk8s kubectl delete --all services --namespace=default
printf "\n"
for filename in Services/*.yaml; do
    printf "Applying $filename\n"
    microk8s kubectl apply -f $filename
done

printf "\n\nDeleting all INGRESS routing...\n"
microk8s kubectl delete --all ingress --namespace=default
printf "\n"
for filename in Ingress/*.yaml; do
    printf "Applying $filename\n"
    microk8s kubectl apply -f $filename
done

printf "\n\nDeleting all DEPLOYMENTS...\n"
microk8s kubectl delete --all deployments --namespace=default
printf "\n"
for filename in Deployments/*.yaml; do
    printf "Applying $filename\n"
    microk8s kubectl apply -f $filename
done

printf "\n\nDeleting all PODS...\n"
microk8s kubectl delete --all pods --namespace=default

printf "\n\nDone.\n"
