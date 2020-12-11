FROM ubuntu:18.04

RUN apt-get -y update && apt-get -y install g++ python3-pip net-tools openjdk-8-jre-headless wget vim
RUN wget "http://apache.claz.org/kafka/2.6.0/kafka_2.13-2.6.0.tgz" 
RUN tar xzf kafka_2.13-2.6.0.tgz -C /opt && mv /opt/kafka_* /opt/kafka

EXPOSE 2181

CMD ["/opt/kafka/bin/zookeeper-server-start.sh","/opt/kafka/config/zookeeper.properties"]