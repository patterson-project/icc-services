#!/bin/bash

microk8s kubernetes delete --all deployments --namespace=default

for filename in Kubernetes/Deployments/*.yaml; do
    mirok8s kubernetes apply -f $filename
done
