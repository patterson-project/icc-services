FROM debian:latest
RUN apt-get update && apt-get upgrade -y

FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /app

RUN pip3 install asyncio-mqtt python-kasa

COPY src/*.py ./

EXPOSE 1883 9999

CMD [ "python", "-u", "bulb_controller.py"] 
