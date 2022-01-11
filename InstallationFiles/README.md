# How to Install

- Add each `.service` file to `/etc/systemd/system/docker-compose-app.service`
- Run the following command for each service:
  - `systemctl enable ServiceName`
    - e.g. `systemctl enable LedApi`
