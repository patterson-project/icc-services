FROM python:buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./src/ ./

ENTRYPOINT [ "python", "-u", "./__main__.py" ]
