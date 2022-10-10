FROM python:buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 8010
EXPOSE 5353

COPY src/*.py ./

ENTRYPOINT [ "python", "-u", "__init__.py" ]
