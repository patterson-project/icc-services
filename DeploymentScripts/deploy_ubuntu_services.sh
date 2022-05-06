sudo systemctl daemon-reload

sudo systemctl enable api.service
sudo systemctl enable bulb-1-controller.service
sudo systemctl enable bulb-2-controller.service
sudo systemctl enable iot-control-center-ui.service

sudo systemctl start api.service
sudo systemctl start bulb-1-controller.service
sudo systemctl start bulb-2-controller.service
sudo systemctl start iot-control-center-ui.service