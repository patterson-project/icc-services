# How to Install

1. Run installation script with `sudo sh ./install.sh` (uncomment lines if docker is not yet installed)

   - This will move systemd scripts into root filesystem and install docker and docker compose (if the respective lines are uncommented in `install.sh`)

2. Enable services on respective raspberry pi's

   - On RaspberryPi Zero W:
     - `systemctl enable led-controller`
   - On RaspberryPi 4:
     - `systemctl enable led-api`
     - `systemctl enable control-center-ui`

3. Now the services will start and automatically update on startup.
