FROM python:buster
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

ENV APP_ENV "production"
ENV MONGO_DB_USERNAME "adrian"
ENV MONGO_DB_PASSWORD "urgarb"

COPY ./src/*.py ./

ENTRYPOINT [ "python", "-u", "./api.py" ]
