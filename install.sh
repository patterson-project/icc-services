#!/bin/bash
cd Api && chmod a+x dockerpush.sh && cd ../
cd BulbController/Bulb1 && chmod a+x dockerpush.sh && cd ../../
cd BulbController/Bulb2 && chmod a+x dockerpush.sh && cd ../../
cd LedController && chmod a+x dockerpush.sh && cd ../
cd IotControlCenterUi && chmod a+x dockerpush.sh && cd ../
chmod a+x update_cluster.sh
