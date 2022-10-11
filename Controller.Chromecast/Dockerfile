FROM python:buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 5000

COPY src/*.py ./

ENTRYPOINT [ "python", "-u", "__init__.py" ]
