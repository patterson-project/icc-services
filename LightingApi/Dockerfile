FROM python:buster
LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

ENV APP_ENV "production"

COPY ./src/*.py ./

ENTRYPOINT [ "python", "-u", "./api.py" ]
