FROM python:3.7-alpine

ENV PYTHONUNBUFFED 1

COPY ./requirements.txt ./requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir nudatu_project
WORKDIR /nudatu_project
COPY ./nudatu_project /nudatu_project

RUN adduser -D nudatu
USER nudatu
