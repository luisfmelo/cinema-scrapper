FROM python:3.7-slim-stretch


RUN apt-get update \
    && apt upgrade -y \
    && apt-get install -y \
    cron \
    build-essential \
    python3-pip \
    nano

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt
RUN chmod -R 755 /src

ENTRYPOINT "/src/entrypoint.sh"