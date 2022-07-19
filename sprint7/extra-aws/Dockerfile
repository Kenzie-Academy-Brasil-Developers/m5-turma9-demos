FROM python:3.10

# PYC
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -U pip

RUN pip install -r requirements.txt

RUN pip install psycopg2

WORKDIR /code

COPY . /code/