FROM python:3.6.1-alpine

RUN apk update \
  && apk add \
    build-base \
    libpq

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV development
ENV FLASK_APP main.py
RUN python setup.py install
CMD ["flask", "run"]
