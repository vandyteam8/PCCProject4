#!/usr/bin/python3

import json
import requests


user="admin"
pword = "vandy"
LOCALHOST = "127.0.0.1"
dbname = "project1"

def couchdbCreateDB(ip):
    baseurl = "http://{user}:{pword}@{ipaddr}:5984/{dbname}".format(user=user, pword=pword, ipaddr=ip, dbname=dbname)
    url = baseurl + dbname
    s = requests.Session()
    s.headers.update({"Content-type": "application/json"})

    response = s.put(url, timeout=100)

if __name__ == '__main__':
    couchdbCreateDB(LOCALHOST)
