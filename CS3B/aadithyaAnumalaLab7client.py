import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

try:
    # connection to hostname on the port.
    s.connect((host, port))
except:
    print("problem connecting to port from client")

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     
s.close()
print (msg.decode('ascii'))
