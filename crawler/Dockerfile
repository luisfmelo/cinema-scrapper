FROM python:3.7-slim-stretch

RUN apt-get update \
    && apt upgrade -y \
    && apt-get install -y \
    cron \
    build-essential \
    python3-pip \
    nano


RUN apt-get install -y libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1

# scrapy and selenium
RUN BUILD_DEPS='autoconf \
                build-essential \
                git \
                libssl-dev' && \
    # the "default-" is important...jessie doesn't have it in the package name
    RUN_DEPS='default-libmysqlclient-dev \
              ca-certificates \
              ssl-cert' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends && \
    pip install --upgrade pip && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

# chrome
RUN BUILD_DEPS='gnupg unzip' && \
    RUN_DEPS='wget' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list && \
    wget https://dl-ssl.google.com/linux/linux_signing_key.pub && \
    apt-key add linux_signing_key.pub && \
    apt-get update && \
    apt-get install -yqq google-chrome-stable --no-install-recommends && \
    rm -rf linux_signing_key.pub && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

# chromedriver
RUN BUILD_DEPS='unzip' && \
    RUN_DEPS='wget' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends cron nano && \
    wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    chmod 755 chromedriver && \
    mv chromedriver /usr/local/bin/chromedriver && \
    rm -rf chromedriver_linux64.zip && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*


COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt
RUN chmod -R 755 /src

ENTRYPOINT ["/src/entrypoint.sh"]