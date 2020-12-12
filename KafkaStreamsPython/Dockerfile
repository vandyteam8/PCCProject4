FROM ubuntu:18.04

COPY ./cons.py /root

ENV IPADDRESS=localhost
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-kafka
RUN apt-get install -y python3-requests

ADD consumer.py ~/consumer.py

CMD ["python3", "~/consumer.py", "$IPADDRESS"]


