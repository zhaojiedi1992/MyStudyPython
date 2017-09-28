import sys,os 
import multiprocessing
from socket_stream_redict import * 
def test_server1():
    pid = os.getpid()
    conn = init_listener_socket()
    file = conn.makefile("r")
    for i int range(3):
        data = file.readline().rstrip()
        print("server %s got [%s]", (pid,data))
def test_client1():
    pid = os.getpid()
    redict_out()
    for i in range(3):
        print("client %s: %s" %(pid,i))
        sys.stdout.flush()

test_server1()
test_client1()
