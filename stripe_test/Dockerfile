FROM python:3.9.4-slim

RUN mkdir /stripe_test

WORKDIR /stripe_test

COPY ./stripe_test/requirements.txt /stripe_test/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY ./stripe_test /stripe_test