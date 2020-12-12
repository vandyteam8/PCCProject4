#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, we use the "top" command and use it as producer of events for
#    Kafka. The consumer can be another Python program that reads and dumps the
#    information into a database OR just keeps displaying the incoming events on the
#    command line consumer (or consumers)
#

import json  # for data
import os  # need this for popen
import sys  # for ipaddr as a command line argumen
import time  # for sleep
from kafka import KafkaProducer  # producer of events
import csv  # reading energy data

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)

def run(ipaddr):
    csvfile= "./energy-sorted1M.csv"

    producer = KafkaProducer (bootstrap_servers="{}:9092".format(ipaddr),
                                    acks=1, value_serializer = lambda v:
                                  json.dumps(v).encode('utf-8'))                                

    #wait for leader to write to log
    #TODO - might be nice to have this as run() argument
    topic = "energyutilization"

    """
    # say we send the contents 100 times after a sleep of 1 sec in between
    for i in range (100):
        print("Loop ", i)
    
        # get the output of the top command
        process = os.popen ("top -n 1 -b")
        
        #ERJ - added CPU time as GMT (not sure where in the world our cloud VMs are)
        #... note that this isn't exactly clock ticks from the os call, but .read() util
        #... isn't exactly deterministic either
        timestamp = time.asctime(time.gmtime(time.time()))
    
        #read the contents that we wish to send as topic content
        contents = process.read ()

        print("Got contents.")

        # send the contents under topic utilizations. Note that it expects
        # the contents in bytes so we convert it to bytes.
        #
        # Note that here I am not serializing the contents into JSON or anything
        # as such but just taking the output as received and sending it as bytes
        # You will need to modify it to send a JSON structure, say something
        # like <timestamp, contents of top>
        #
        """

    with open(csvfile, encoding='utf=8') as csvf:
        csvReader = csv.reader(csvf)
        # id,ts,val,prop,pid,hhid,hid
        # ex.[1,1377986401,68.451,0,11,0,0]

        for row in csvReader:
            # uid={h, hhidpid}
            print(row)
            key = [str(row[6]), str(row[5]) + str(row[0])] #tuple-dict as key
            data = {
                'id': int(row[0]),
                'timestamp': int(row[1]),
                'value': float(row[2]),
                'property': int(row[3]),
                'plug_id': int(row[4]),
                'household_id': int(row[5]),
                'house_id': int(row[6])
            }

        print(key, data)
        timestamp = time.asctime(time.gmtime(time.time()))

        producer.send (topic,
        {'topic' : topic, 
        'timestamp': timestamp, 
        'key': key,
         'data': data})

        print("Sending")
        producer.flush()   # try to empty the sending buffer
        print("Sleeping")
        # sleep a second
        time.sleep (1)

    # we are done
    producer.close ()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ipaddr = sys.argv[1]
        print("Running with IP address: {}".format(ipaddr))
        run(ipaddr)
    else:
        ipaddr = '127.0.0.1'
        run(ipaddr)






