sudo systemctl daemon-reload

sudo systemctl enable api.service
sudo systemctl enable bulb-1-controller.service
sudo systemctl enable bulb-2-controller.service
sudo systemctl enable iot-control-center-ui.service

sudo systemctl restart api.service
sudo systemctl restart bulb-1-controller.service
sudo systemctl restart bulb-2-controller.service
sudo systemctl restart iot-control-center-ui.service
