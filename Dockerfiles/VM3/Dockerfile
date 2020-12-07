FROM ubuntu:latest


RUN apt-get update
RUN apt-get install -y default-jre
RUN apt-get install -y default-jdk
RUN apt-get install -y python3
RUN apt-get install -y python3-kafka
RUN apt-get install -y python3-requests

ADD consumer.py ~/consumer.py


CMD ["python3", "~/consumer.py", "34.195.182.141"]
