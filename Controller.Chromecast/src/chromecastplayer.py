from config import Config
import pychromecast


class ChromecastPlayer:
    def __init__(self, chromecast: pychromecast.Chromecast):
        self.chromecast = chromecast
        self.chromecast.wait()
        print(f"{self.chromecast.cast_info.host} initialized")

    def cast_media(self, path: str):
        self.chromecast.media_controller.play_media(
            f"{Config.MEDIA_DRIVE_SERVICE_URL}/{path}", content_type="video/mp4")
        self.chromecast.media_controller.block_until_active()
        self.chromecast.media_controller.play()
