#!/bin/sh

# Bootstrapping steps. Here we create needed directories on the guest
mkdir -p ~/.ssh
mkdir -p ~/.ansible
mkdir -p ~/.config
mkdir -p ~/.config/openstack
add-apt-repository universe
apt-get update
apt-get install python3-pip -y
pip3 install future
pip3 install ansible
pip3 install openstacksdk
python3 -m pip install --upgrade pip setuptools wheel
ansible-galaxy collection install openstack.cloud

