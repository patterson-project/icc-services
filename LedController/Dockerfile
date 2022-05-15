FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY /src/*.py ./

EXPOSE 1883
ENV BROKER_IP=10.0.0.68

CMD [ "python", "led_strip_controller.py"]
