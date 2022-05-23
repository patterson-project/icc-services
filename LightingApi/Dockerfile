FROM python:buster
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

ENV MONGO_DB_USERNAME ${MONGO_DB_USERNAME}
ENV MONGO_DB_PASSWORD ${MONGO_DB_PASSWORD}

COPY ./src/*.py ./

ENTRYPOINT [ "python", "-u", "./api.py" ]