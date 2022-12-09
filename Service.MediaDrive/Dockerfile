FROM python:3.10-slim-bullseye

WORKDIR /app

EXPOSE 8000 

ENTRYPOINT [ "python", "-u", "-m", "http.server", "8000", "--bind", "0.0.0.0" ]
