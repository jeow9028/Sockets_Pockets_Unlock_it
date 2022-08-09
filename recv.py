# recv.py
#Importing
import socket
from time import sleep

# Open source file/functions for socket
# help(socket)


s = socket.socket()
host = ''
port = 19132
s.bind((host, port))

print( "host = Open", host, "\r\n", "port = ", port)

# Path of file
# path = "C:/Users/jeanchri/OneDrive-Advanced Micro Devices Inc/Documents/Github/TCP/Sockets_Pockets_Unlock_it"
# f = open(path, 'wb')
# Wait for Client Connection
s.listen() 

while True:
	# Establish Connection
	c, addr = s.accept()
	print("Recv Connection", addr)
	print("Receiving......")
	l = c.recv(1024)
	while True:
		print("Receiving......")
		f.write(1)
		l = c.recv(1024)
	f.close()
	print("Done receiving")
	c.close





