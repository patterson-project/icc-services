import os
import subprocess


class ChromecastPlayer:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def cast_media(self, path: str):
        cast_command = "cvlc -vvv --sout=\"#chromecast{ip=" + self.ip_address + \
            "}\" --demux-filter=demux_chromecast \"" + path + "\""
        print(cast_command)
        subprocess.Popen(cast_command)
