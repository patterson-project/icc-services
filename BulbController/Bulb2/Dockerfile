FROM python:latest
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY src/*.py ./

EXPOSE 1883 9999
ENV BROKER_IP=10.0.0.68
ENV BULB_IP=10.0.0.37
ENV BULB_TOPIC=bulb-2

ENTRYPOINT [ "python", "-u", "bulb_controller.py" ] 
