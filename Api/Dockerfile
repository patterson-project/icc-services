FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./src/*.py ./

EXPOSE 8000

ENTRYPOINT [ "python", "./api.py" ]