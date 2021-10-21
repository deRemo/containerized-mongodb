#!/usr/bin/python3
import os

os.system("sudo docker build . -f Dockerfile.env -t rt-mongod-env")
os.system("sudo docker build . -f Dockerfile.build -t rt-mongod-build")
os.system("sudo docker build . -f Dockerfile.run -t rt-mongod")
