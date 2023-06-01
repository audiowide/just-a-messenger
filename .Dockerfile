FROM python:3.10.10

ENV PYTHONUNBUFFERED 1

RUN mkdir app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD . /app/
ADD .env.docker /app/.env

ENV APP_NAME=simple_messager

COPY . .
CMD gunicorn demo.wsgi:application -b 0.0.0.0:8080