# dockerized-mongodb
<p align="center">
  <img src="https://github.com/deRemo/dockerized-mongodb/blob/main/sample_img.png?raw=true" alt="Container network"/>
</p>

The purpose of this repo is to show how to dockerize MongoDB from scratch and
how to configure a replica set between multiple dockerized mongod instances.

Utility tool for my research project RT-MongoDB (https://gitlab.retis.santannapisa.it/t.cucinotta/mongo/-/tree/v4.4-rt)

**NOTE**: This tool is designed for RT-MongoDB, thus it makes use of tuning server parameters that do not exist on the original MongoDB

# Example of usage with 2 replica nodes
Clone the repo on both hosts, make sure that the Python scripts are executable and the hosts reachable, then:
```
 user@primary_host:~/dockerized-mongodb$ ./build_images.py
 user@primary_host:~/dockerized-mongodb$ ./run.py
 
 user@secondary_host:~/dockerized-mongodb$ ./build_images.py
 user@secondary_host:~/dockerized-mongodb$ ./run.py
 
 user@primary_host:~/dockerized-mongodb$ ./configure_rs.py ip_primary ip_secondary
 ```
 
 Now you can interact with the database:
 ```
 user@primary_host:~/dockerized-mongodb$ mongo --host primary_host  //YOU CAN NOW INTERACT WITH THE DATABASE
 ```
 
 # Warning
 Any changes to the files may compromise the basic functionality of the software
