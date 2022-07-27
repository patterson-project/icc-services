FROM python:buster
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

ENV BULB_1_IP=10.0.0.90
ENV BULB_2_IP=10.0.0.37
ENV MONGO_DB_USERNAME "adrian"
ENV MONGO_DB_PASSWORD "urgarb"

COPY src/*.py ./

ENTRYPOINT [ "python", "-u", "__init__.py" ]
