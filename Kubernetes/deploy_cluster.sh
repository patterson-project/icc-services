#!/bin/bash
printf "Deleting all SERVICES...\n"
kubectl delete --all services --namespace=default

printf "\n"
for filename in Services/*.yaml; do
    printf "Applying $filename\n"
    kubectl apply -f $filename
done

printf "\n\nDeleting all INGRESS routing...\n"
kubectl delete --all ingress --namespace=default
printf "\n"
for filename in Ingress/*.yaml; do
    printf "Applying $filename\n"
    kubectl apply -f $filename
done

printf "\n\nDeleting all DEPLOYMENTS...\n"
kubectl delete --all deployments --namespace=default
printf "\n"
for filename in Deployments/*.yaml; do
    printf "Applying $filename\n"
    kubectl apply -f $filename
done

printf "\n\nDeleting all PODS...\n"
kubectl delete --all pods --namespace=default

printf "\n\nDone.\n"

for filename in Services/*.yaml; do
    printf "Applying $filename\n"
    kubectl apply -f $filename
done

printf "\n\nDeleting all INGRESS routing...\n"
kubectl delete --all ingress --namespace=default
printf "\n"
for filename in Ingress/*.yaml; do
    printf "Applying $filename\n"
    kubectl apply -f $filename
done

printf "\n\nDeleting all DEPLOYMENTS...\n"
kubectl delete --all deployments --namespace=default
printf "\n"
for filename in Deployments/*.yaml; do
    printf "Applying $filename\n"
    kubectl apply -f $filename
done

printf "\n\nDeleting all PODS...\n"
kubectl delete --all pods --namespace=default

printf "\n\nDone.\n"
