FROM ubuntu:18.04

COPY ./consumer.py /root
# ENV IPADDRESS=localhost

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-kafka
RUN apt-get install -y python3-requests
RUN apt-get install -y socket

# ADD consumer.py ~/consumer.py

CMD ["python3", "/root/consumer.py", "34.195.182.141"]
