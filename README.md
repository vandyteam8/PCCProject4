# PCCProject3

Control Flow
* SSH into our 2 AWS instances. (VM2 and VM3)
* Build the Dockerfile in VM2 
    docker build .
* Run the docker compose file in VM2:
    docker-compose up -d
* Follow the same steps for VM3 that were used for VM2
* On your local VM, run producer.py:
    python3 producer.py <floating IP VM2/VM3>
* Navigate to: http://34.195.182.141:5984/_utils/#login (user: admin, pw: vandy)
