FROM python:3.7-slim-stretch

RUN apt-get update \
    && apt upgrade -y \
    && apt-get install -y \
    build-essential \
    python3-pip \
    nano

RUN pip install --upgrade pip

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

CMD [ "python", "-u", "consumer.py" ]