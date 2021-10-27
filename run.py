#!/usr/bin/python3
import os,socket

def get_ip():
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
		s.connect(("8.8.8.8", 80))
		return s.getsockname()[0]

def get_pwd():
	return os.path.abspath(os.getcwd())

os.system(f"sudo docker run --name rt-mongod --rm -d -p {get_ip()}:27017:27017 -v {get_pwd()}/cfg:/cfg -it rt-mongod")
