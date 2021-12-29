FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /usr/app

RUN pip3 install flask &&  \
    pip3 install requests &&  \
    pip3 install rpi_ws281x

COPY *.py ./

EXPOSE 5000
CMD [ "python", "./led_api.py"]