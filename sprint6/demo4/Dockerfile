FROM python:3.10

# .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /code

COPY . /code/

# run ./manage.py migrate

# Não preciso quando utilizando compose
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]