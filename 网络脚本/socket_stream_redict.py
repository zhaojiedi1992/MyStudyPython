import sys
from socket import * 

port=50008
host='localhost'

def init_listener_socket(port= port):
    sock = socket(family=AF_INET,type=SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(5)
    conn,addr = sock.accept()
    return conn
def redict_out(port =port ,host=host):
    sock = socket(family=AF_INET,type=SOCK_STREAM)
    sock.connect((host,port))
    file=sock.makefile('w')
    sys.stdout=file
    return sock
def redict_in(port =port ,host=host):
    sock = socket(family=AF_INET,type=SOCK_STREAM)
    sock.connect((host,port))
    file=sock.makefile('r')
    sys.stdinfile
    return sock
def redict_in_and_out_for_client(port=port,host=host):
    sock = socket(family=AF_INET,type=SOCK_STREAM)
    sock.connect((host,port))
    out_file = sock.makefile("w")
    in_file = sock.makefile("r")
    sys.stdin= in_file
    sys.stdout = out_file
    return sock
def redict_in_and_out_for_server(port=port,host=host):
    sock = socket(family=AF_INET,type=SOCK_STREAM)
    sock.bin((host,port))
    sock.listen(5)
    conn,addr = sock.accept()
    out_file = sock.makefile("w")
    in_file = sock.makefile("r")
    sys.stdin= in_file
    sys.stdout = out_file
    return sock