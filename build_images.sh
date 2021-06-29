#!/bin/bash

sudo docker build . -f Dockerfile.env -t rt-mongod-env
sudo docker build . -f Dockerfile.build -t rt-mongod-build
sudo docker build . -f Dockerfile.run -t rt-mongod
