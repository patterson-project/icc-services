FROM python:buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

COPY src/*.py ./

RUN sudo apt-get update && sudo apt-get install vlc

ENTRYPOINT [ "python", "-u", "__init__.py" ]
