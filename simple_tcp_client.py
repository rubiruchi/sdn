import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('10.0.0.100', 4444))

data = "Hello" 

sock.send(data)


data = sock.recv(100)

print data

sock.close()
