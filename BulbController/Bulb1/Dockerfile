FROM python:latest
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY src/*.py ./

ENV BROKER_IP=10.0.0.34
ENV BROKER_PORT=1884
ENV BULB_IP=10.0.0.90
ENV BULB_TOPIC=bulb-1

ENTRYPOINT [ "python", "-u", "bulb_controller.py" ] 
