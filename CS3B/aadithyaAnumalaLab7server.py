###############################################
# CS 21B Intermediate Python Programming Lab #7
# Topics: Web Programming
# Description: This program creates a server-
#              client system using sockets of hosts
#              and ports to send simple messages
#              affirming the mutual connection
#              built.
# Input: none
# Output: connection
# Version: 3.7.0
# Development Environment:  IDLE
# Developer:  Aadithya Anumala
# Student ID: 20365071
# Date:  06/04/19
###############################################

import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

try:
    serversocket.bind((host, port))
except:
    print("problem connecting to port from server")

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("connected with the client %s" % str(addr))
    
   msg = 'Connected with server'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   
   clientsocket.close()
