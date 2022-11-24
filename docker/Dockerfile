FROM python:3.10.4-slim-buster
COPY requirements.txt /tmp
RUN apt-get update && apt install net-tools -y && apt install curl -y  && apt-get install -y build-essential sudo libpq-dev libmariadb-dev libffi-dev libssl-dev libcurl4-openssl-dev rustc
RUN \
    pip install --upgrade pip && \
    pip wheel --wheel-dir /wheels apprise uwsgi mysqlclient minio -r /tmp/requirements.txt
COPY . /opt/healthchecks/
RUN rm -rf /opt/healthchecks/.git
ENV PYTHONUNBUFFERED=1
WORKDIR /opt/healthchecks
RUN \
    apt update && \
    apt install -y libpq5 libmariadb3 && \
    rm -rf /var/apt/cache
RUN \
    pip install --upgrade pip && \
    pip install --no-cache /wheels/*
RUN \
    rm -f /opt/healthchecks/hc/local_settings.py && \
    DEBUG=False SECRET_KEY=build-key ./manage.py collectstatic --noinput && \
    DEBUG=False SECRET_KEY=build-key ./manage.py compress
USER root
CMD [ "uwsgi", "/opt/healthchecks/docker/uwsgi.ini"]
