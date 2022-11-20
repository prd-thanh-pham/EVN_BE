FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get upgrade -y && apt-get install sudo
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
