FROM python:3.8-slim

WORKDIR /app

RUN apt-get -qq update && \
    apt-get -qq install make

COPY . /app

RUN pip install --upgrade pip wheel setuptools poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

RUN apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

ARG BUILD_DATETIME
ARG SHA1
ARG VERSION

LABEL io.github.mbeacom.description="CloudEndure CLI and API client module" \
    io.github.mbeacom.documentation="https://mbeacom.github.io/cloudendure-python/" \
    io.github.mbeacom.licenses="MIT" \
    io.github.mbeacom.image.revision=$SHA1 \
    io.github.mbeacom.image.version=$VERSION \
    io.github.mbeacom.image.vendor="mbeacom" \
    io.github.mbeacom.image.source="https://github.com/mbeacom/cloudendure-python" \
    io.github.mbeacom.image.title="CloudEndure Client" \
    io.github.mbeacom.image.created=$BUILD_DATETIME
