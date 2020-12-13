# Author: Aniruddha Gokhale
# Vanderbilt University
# Created Nov 2017
#
# For Cloud Computing class
#
# Docker build file for our MapReduce master
#

# First, use the latest ubuntu image
FROM ubuntu:18.04
#

# Now install the needed python and other packages
RUN apt-get -y update && apt-get install -y net-tools iputils-ping python3


# The following may not be needed but we let it be there.
RUN apt-get install -y python3-dev python3-pip
RUN python3 -m pip install --upgrade pip

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# Install the zeromq package
RUN apt-get install -y python3-zmq
RUN apt-get install -y python3-pandas
RUN apt-get install -y python-couchdb

# Next, copy the files needed to run the map-reduce master
COPY mr_energy.py /root/
COPY mr_framework.py /root/
COPY mr_thread.py /root/

#
# Run a command shell
# Note that we do not run the wordcount directly as the service
# in our swarm otherwise when the wordcount completes, the container
# will die. So we manually do a "docker exec" from a separate shell
# while allowing the service to start this container with just a shell
CMD /bin/bash
