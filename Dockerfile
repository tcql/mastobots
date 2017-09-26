FROM ubuntu:16.04

WORKDIR /usr/local/src/bots

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install ananas

EXPOSE 443
ADD . .

CMD ["/bin/bash", "-c", "./worker.sh"]
