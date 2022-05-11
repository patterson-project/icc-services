#!/bin/bash
cd Api && sh dockerpush.sh && cd ../
cd BulbController/Bulb1 && sh dockerpush.sh && cd ../../
cd BulbController/Bulb2 && sh dockerpush.sh && cd ../../
cd LedController && sh dockerpush.sh && cd ../
cd IotControlCenterUi && sh dockerpush.sh && cd ../

microk8s kubernetes delete --all pods --namespace=default