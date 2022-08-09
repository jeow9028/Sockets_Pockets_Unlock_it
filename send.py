# TCP/IP Send and Receive

# **********************
#!/usr/bin/python
# ports open: [ -- 19132 (UDP) ]
#             [  -- 25564 (TCP)]   
# **********************

import socket #import socket module

print("Creating Connection")

s = socket.socket() #create a socket object

host = '172.19.68.201' #Host i.p
port = 19132 #Reserve a port for your service

s.connect((host,port))
print(s.recv(1024))
s.close