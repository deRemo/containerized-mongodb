#!/usr/bin/python3
import os,socket

os.system(f"sudo docker exec -it rt-mongod ./mongo --host $(hostname)")
