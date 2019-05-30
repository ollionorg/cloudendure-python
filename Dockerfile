FROM python:3.7.3-slim-stretch

WORKDIR /app

ARG SYSTEM_PACKAGES="make"

RUN apt-get -qq update
RUN apt-get -qq upgrade
RUN apt-get -qq install ${SYSTEM_PACKAGES}

COPY . /app

RUN pip install --upgrade pip
RUN pip install --upgrade wheel setuptools twine pipenv
RUN pipenv install --dev --system --deploy

RUN apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/
