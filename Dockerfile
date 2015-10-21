FROM alpine:3.1

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    libuuid \
  && rm -rf /var/cache/apk/*

WORKDIR /search

ADD . /search
RUN pip install -r /search/requirements.txt

EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-w", "8", "-b", "0.0.0.0:5000", "app:app" ]
