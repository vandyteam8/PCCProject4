FROM ubuntu:18.04

RUN apt-get -y update && apt-get -y install g++ python3-pip net-tools openjdk-8-jre-headless wget 
RUN wget "http://apache.claz.org/kafka/2.6.0/kafka_2.13-2.6.0.tgz" 
RUN tar xzf kafka_2.13-2.6.0.tgz -C /opt && mv /opt/kafka_* /opt/kafka

RUN echo "auto.create.topics.enabled=1 \n\
listeners=PLAINTEXT://:9092 \n\
advertised.listeners=PLAINTEXT://129.114.26.88:9092 \n\
broker.id.generation.enable=true \n\
listener.security.protocol.map=PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL \n\
num.network.threads=3 \n\
num.io.threads=8 \n\
socket.send.buffer.bytes=102400 \n\
socket.receive.buffer.bytes=102400 \n\
socket.request.max.bytes=104857600 \n\
log.dirs=/tmp/kafka-logs \n\
num.partitions=1 \n\
num.recovery.threads.per.data.dir=1 \n\
offsets.topic.replication.factor=1 \n\
transaction.state.log.replication.factor=1 \n\
transaction.state.log.min.isr=1 \n\
log.retention.hours=168 \n\
log.segment.bytes=1073741824 \n\
log.retention.check.interval.ms=300000 \n\
zookeeper.connect=127.0.0.1:2181 \n\
zookeeper.connection.timeout.ms=18000 \n\
group.initial.rebalance.delay.ms=0" > /opt/kafka/config/server.properties

RUN echo "#!/bin/bash \n\
/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties" > /opt/startkafka.sh

EXPOSE 9092

RUN chmod +x /opt/startkafka.sh

CMD ["/opt/startkafka.sh"]

