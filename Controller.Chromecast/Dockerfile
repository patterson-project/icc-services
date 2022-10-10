FROM python:buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 8010

COPY src/*.py ./

RUN apt update
RUN apt -y install vlc
RUN sed -i 's/geteuid/getppid/' /usr/bin/vlc

ENTRYPOINT [ "python", "-u", "__init__.py" ]
