# PCCProject2

Control Flow  
* Issue "vagrant up" command in the AnsibleVagrantScaffold directory  
* Vagrant reads Vagrantfile  
  * Vagrantfile copies files from the directory into the Vagrant image  
  * Vagrantfile also runs a shell script that install some packages like openstack  
  * Vagrantfile then launches Ansible provision  
* Ansible playbook launches with playbook_demo_master.yml  
  * Ansible gets local VM facts  
  * Ansible then includes playbook_start_chameleon.yml which spins up the Chameleon Cloud  
  * Then use playbook_install_cloud.yml to install Kafka/Zookeeper  
  * ###MISSING### Playbook_zookeeper.yml should start Zookeeper on VM2  
  * ###MISSING### playbook_kafka.yml should start Kafka on both VMs  
  * ##NOT WORKING## playbook_couchdb.yml should install CouchDB on VM3  
  * ##MISSING## playbook_consumer.yml should start consumer.py on VM 2 & VM3  
  * ##MISSING## Ansible should start producer.py on Vagrant  

- Also need to have a way to see the CouchDB server, ideally without checking Floating IP with Chameleon Cloud  
