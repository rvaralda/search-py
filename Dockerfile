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

COPY ./appdynamics.cfg /etc/appdynamics.cfg

EXPOSE 5000
CMD /env/bin/python run.py
