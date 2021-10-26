#!/usr/bin/python3
import os

os.system("sudo docker build . -f ./MongoDB/Dockerfile.env -t rt-mongod-env")
os.system("sudo docker build . -f ./MongoDB/Dockerfile.build -t rt-mongod-build")
os.system("sudo docker build . -f ./MongoDB/Dockerfile.run -t rt-mongod")
