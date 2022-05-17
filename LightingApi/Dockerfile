FROM python:latest
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./src/*.py ./

EXPOSE 8000
ENV BROKER_IP=10.0.0.34
ENV BROKER_PORT=1884

ENTRYPOINT [ "python", "-u", "./api.py" ]