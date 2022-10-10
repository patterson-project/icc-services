import os


class ChromecastPlayer:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def cast_media(self, path: str):
        os.system(
            "cvlc -vvv --sout=\"#chromecast{ip=" + self.ip_address + "}\" --demux-filter=demux_chromecast \"" + path + "\"")
