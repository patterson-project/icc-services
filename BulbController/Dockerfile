FROM python:buster
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY src/*.py ./

EXPOSE 5000

ENV BULB_1_IP=10.0.0.90
ENV BULB_2_IP=10.0.0.37

ENTRYPOINT [ "python", "-u", "bulbserver.py" ] 
