#!/usr/bin/python3

import os,sys

if len(sys.argv) < 2:
	print("USAGE: ./script ip1 ip2 ... (hostname are also valid, if recognised)")
	exit()

print("Configuring replica set...")

members = []

for i in range(1, len(sys.argv)):
	prio = 1 if i == 1 else 0 #prioritize first member for the primary election
	members.append("{_id: "+str(i-1)+", host: \'"+str(sys.argv[i])+"\', priority: "+str(prio)+"}")

#stringify members and prepare rs config
members = ', '.join(d for d in members)
cfg = "{_id: 'rs0', members: ["+members+"]}"
	
	
print(cfg)
inner_cmd = "./mongo --host "+sys.argv[1]+" --eval \"JSON.stringify(db.adminCommand({'replSetInitiate' : "+cfg+"}))\""
outer_cmd = "sudo docker exec -it rt-mongod bash -c '"+inner_cmd+"'"

os.system(outer_cmd)
