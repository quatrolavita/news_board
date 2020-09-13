FROM python:3.8-alpine
MAINTAINER OLEKSANDR LAVRUSENKO

ENV PYTHONUNBUFFERED 1
COPY ./req.txt ./req.txt
RUN apk add  --no-cache postgresql-client
RUN apk add  --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev gcc musl-dev libffi-dev openssl-dev python3-dev
RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install  --no-cache-dir -r /req.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D user
USER user

CMD gunicorn news_board.wsgi:application --bind 0.0.0.0:$PORT