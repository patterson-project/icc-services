# Iot Control Center

A local area network kubernetes cluster for managing and controlling IoT devices.

# Installation

1. Flash an SD card with **Ubuntu Server OS Arm64 Architecture**

   - Can be done using the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   - Before flashing, configure the network connection settings and enable SSH to allow the Pi connection to the internet
   - Alternatively, this can be done manually by editing the `/etc/netplan/50-cloud-init.yaml` found in Ubuntu

---

2. Boot up the Raspberry Pi and SSH into it

---

3. Docker and docker-compose Installation

   - [Docker Installation on Ubuntu Docs](https://docs.docker.com/engine/install/ubuntu/#install-docker-engine)
   - Allow docker **rootless** permissions for docker and docker-compose, or build scripts will not work

---

4. Login to a [dockerhub](https://hub.docker.com/) account

   - If you do not already have a dockerhub account, create one since it is needed
   - Log in with the `docker login` command
   - In the [dockerhub portal](https://hub.docker.com/), **create a project** called `iot-control-center`

---

5. Install Kubernetes

   - [Rancher Docs](https://rancher.com/docs/k3s/latest/en/installation/install-options/)
     - Default installation can be done with the following command:
       - `curl -sfL https://get.k3s.io | sh -`
   - [Enable cgroups](https://rancher.com/docs/k3s/latest/en/advanced/#enabling-cgroups-for-raspberry-pi-os)
   - Install [linux-modules-extra-raspi](https://rancher.com/docs/k3s/latest/en/advanced/#enabling-cgroups-for-raspberry-pi-os) with:
     - `sudo apt install linux-modules-extra-raspi`
   - Configure DNS
      - Use a text editor to add the following to `/etc/resolv.conf`:
      ```sh 
         namespace 8.8.8.8
         namespace 8.8.4.4
      ```   
      - Then, restart daemon and docker systemctl services
      ```sh
         sudo systemctl daemon-reload
         sudo systemctl restart docker
      ```
      - Purge the DNS pod in the `kube-system` namespace
         - Get the DNS pod name with `kubectl get pods --all-namespaces`, e.g. `coredns-b96499967-ggsj5`
         - Delete it
            - `kubectl delete pods coredns-b96499967-ggsj5 --namespace="kube-system"`     

---

6. Set up your environment variables

- There are 4 environment variables needed for the build script to work:

  1.  `MONGO_DB_USERNAME`
      - Your chosen database username
  2.  `MONGO_DB_PASSWORD`
      - Your chosen database password
  3.  `MONGO_DB_IP`
      - The IP address of the raspberry pi (which hosts the database)
      - This IP address can be found by running `ifconfig`
  4.  `DOCKERHUB_USERNAME`
      - The username of the dockerhub account logged into in step 4

- These environment variables can be set by appending the following to your `~/.bashrc` file:

  ```sh
  export MONGO_DB_USERNAME="<your chosen database username>"
  export MONGO_DB_PASSWORD="<your chosen database password>"
  export MONGO_DB_IP="<the IP of the pi>"
  export DOCKERHUB_USERNAME="<your dockerhub username>"
  ```

---

7. Clone this Repository

---

8. Build and push the local docker containers to dockerhub

   - `cd` into the `/Kubernetes` folder of this repo
   - Execute the `update_cluster.sh` script to build and push all containers
      - This may take quite some time on the first go. Depending on your RPi specs, could take anywhere from 5-20 minutes

---

9. Configure your cluster secrets

   - Copy the `secrets.yaml` found under `/Kubernetes/Secrets`. Rename it to `secrets.yaml` or another name of your choosing
   - Edit the file with a text editor to add the secrets. You'll need to add:
     - A Mongo Database Username and Password
     - The address of the Mongo Database (i.e. the address of the current Raspberry Pi. This can be found using `ifconfig`)
   - Apply the secrets to your cluster using `kubernetes apply -f secrets.yaml`

---

10. Deploy the Mongo Database

- Build and bring up the docker container for the database
  - `cd` into `/MongoDb`
  - Run `docker-compose up --build -d`
- To validate, visit the IP address at port 8081 to validate the mongo express UI appears
  - e.g. `http://10.0.0.4:8081`

---

11. Deploy the cluster

    - `cd` into `/Kubernetes`
    - Run `deploy_cluster.sh` to deploy the cluster
    - Check your device IP from anywhere on your LAN, you should see the IoT Control Center Home page!

---

<p align="center">
<image src="https://user-images.githubusercontent.com/47571939/151073711-508f1d52-cf0e-45ec-99c4-fd5c7f7579c4.png">
</p>
