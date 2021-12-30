FROM ubuntu:latest
RUN apt update -y && apt upgrade -y

FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /usr/app

RUN pip3 install flask requests json

COPY src/*.py ./

EXPOSE 8000
CMD [ "python", "-u", "api.py"]