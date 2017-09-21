from socket import *
HOST='localhost'
PORT=50007

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
            