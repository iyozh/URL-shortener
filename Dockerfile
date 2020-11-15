FROM python:3.8-alpine

ENV ENV_FOR_DYNACONF development

RUN apk --no-cache --update --virtual build-dependencies add \
    bash \
    g++ \
    libffi-dev \
    make \
    postgresql-dev \
    python3-dev \
    || exit 1

RUN pip install pipenv

WORKDIR /app/

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pipenv install --deploy

COPY ./ ./