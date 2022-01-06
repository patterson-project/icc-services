from datetime import datetime


def log(message):
    now = datetime.now()
    print(str(now.strftime('%Y-%m-%d %H:%M:%S')), end="")
    print(message)
