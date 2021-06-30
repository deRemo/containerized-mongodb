#!/bin/bash

if [ $# -lt 2 ]; then
	echo "USAGE: ./script ip1 ip2 (hostname are also valid, if recognised)" 
	exit 1
fi

echo "configuring replica set"

cfg="{
    _id: 'rs0',
    members: [{_id: 0, host: '$1:27017', priority:1}, 
              {_id: 1, host: '$2:27017', priority:0}] 
}"

#configure rs
echo $cfg

sudo docker exec -it rt-mongod bash -c "./mongo --host $1 --eval \"JSON.stringify(db.adminCommand({'replSetInitiate' : $cfg}))\""
