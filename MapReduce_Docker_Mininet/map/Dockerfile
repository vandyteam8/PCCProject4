# Author: Aniruddha Gokhale
# Vanderbilt University
# Created Nov 2017
#
# For Cloud Computing class
#
#
# Docker build file for our Map worker
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
RUN pip install CouchDB

#
# Next, copy the files needed to run the map-reduce master
COPY mr_mapworker.py /root/

# The map worker will be started when the service is created with a
# command line which will be of the form
# python /root/mr_mapworker.py <master IP addr> <master port> 
