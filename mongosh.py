#!/usr/bin/python3
import os

#Interact with the mongod instance locally using mongo shell
os.system(f"sudo docker exec -it rt-mongod ./mongo --host $(hostname)")
