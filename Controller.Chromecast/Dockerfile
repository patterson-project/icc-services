FROM python:3.10-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 5000

COPY ./src/ ./

ENTRYPOINT [ "python", "-u", "__main__.py" ]
