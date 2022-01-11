curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

cd /ControlCenterUi/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh

cd ../LedApi/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh

cd ../LedControl/ShellScripts
sudo chmod 744 start.sh
sudo chmod 744 stop.sh

cp /SystemdFiles/* /etc/systemd/system/