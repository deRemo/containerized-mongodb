#!/bin/bash
set -x
sudo docker run --name rt-mongod --rm -p $(hostname -i | awk '{print $1}'):27017:27017 -it rt-mongod
