FROM ubuntu:16.04

WORKDIR /usr/local/src/bots

RUN apt-get update
RUN apt-get install -y python3 python3-pip libjpeg-dev
RUN pip3 install ananas Pillow numpy

EXPOSE 443
ADD . .

CMD ["/bin/bash", "-c", "./worker.sh"]
