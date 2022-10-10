FROM python:buster

WORKDIR /app

EXPOSE 8000

ENTRYPOINT [ "python", "-u", "-m", "http.server", "localhost:8000", "--bind", "0.0.0.0" ]
