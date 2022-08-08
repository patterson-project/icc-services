FROM python:buster

LABEL Maintainer="canadrian72"

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

ENV MONGO_DB_USERNAME "adrian"
ENV MONGO_DB_PASSWORD "urgarb"

COPY /src/*.py ./

CMD [ "python", "-u", "__init__.py"]
