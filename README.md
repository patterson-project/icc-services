# Home LED Control Center

A set of docker-based services which use Raspberry Pis and MQTT to control WS2811 LED strips.

## Repository Structure

- `/IotControlCenterUi`
  - Holds React-Typescript app for user interface
- `/Api`
  - Holds flask API to handle UI calls and publish MQTT messages to IoT devices accordingly
- `/LedController`
  - Holds python service to listen for MQTT events and change LED strip behavior accordingly
- `/BulbController`
  - Holds python service to listen for MQTT events and change TPLink kasa-smart bulb behavior accordingly
- `/SystemdFiles`
  - Systemd service configuration files to allow each microservice to be automatically deployed and updated startup on raspberry pi boot
- `install.sh`
  - Copies Systemd configuration files into `/etc/systemd/systm/` of raspberry pis
  - Makes `start.sh` and `stop.sh` scripts executable

## IotControlCenterUi

- React-Typescript web app hosted with an nginx server
- Docker compose file used to build react app and host on nginx
- All components found in `/src`
- Look of web-page:

<p align="center">
<image src="https://user-images.githubusercontent.com/47571939/165000409-ac0a3dea-c6bd-47ba-8e7b-fbc39a63c5c4.png">
</p>
 <p align="center">
<image src="https://user-images.githubusercontent.com/47571939/165000413-6a617da4-144f-4c0c-9eb6-fb35e98e3c34.png">
</p>
  
* Allows to change LED strip color, brightness, and activate different sequences

## Api

- Flask API to provide endpoints to activate different commands
- After each route is called, MQTT is used to publish this command to the other raspberry pi
  - e.g the LED route publishs an object of type `LedRequest` as a dictionary with options for LED command (i.e. brightness, HSV values, operation)
- Docker compose file used to build dockerfile to host and expose the flask API

## LedController

- Holds code which actually interfaces with LED strip
  - `led_operation.py` contains functions to execute different operations on the LEDs (e.g. rainbow, change brightness, set all pixels as RGB value, etc.)
  - `mqtt_client.py` starts an MQTT client to listen for publish events from flask API
- Docker compose builds docker file to host and expose service on local area network

## SystemdFiles

- Holds configuration files for each service
  - Allows each service to be automatically started on boot

## install.sh

- Each service has a folder called `/ShellScripts`
  - These scripts start and stop the service by calling `docker-compose up ...` or `docker-compose down ...` respectively
- Install .sh makes each shell script executable and moves Systemd files into the root file system

## Hardware

### Raspberry Pi 4 with Ubuntu server OS

- Runs the **LedApi** and **IotControlCenterUi** services

<p align="center">
<image src="https://user-images.githubusercontent.com/47571939/151073711-508f1d52-cf0e-45ec-99c4-fd5c7f7579c4.png">
</p>
    
### Raspberry Pi Zero W
  * Runs the **LedController** service

<p align="center">
<image src="https://user-images.githubusercontent.com/47571939/151073762-67bad429-5483-4f62-b2af-727edb21bb57.png">
</p>
  
* Installation specific to these two devices found in `/SystemdFiles/README.md`
  
### WS2811 LED Strip
* Interfaces with raspberry pi zero w GPIO pin 18
  * LED Config found in utils in the `LedController` service
  
<p align="center">
<image src="https://user-images.githubusercontent.com/47571939/151074248-d8d76d5a-f586-437f-8991-516312ab2b83.png">
</p>
