import time
import threading
from socket import * 

host=''
port=50007

obj=socket(family=AF_INET,type=SOCK_STREAM)
obj.bind((host,port))
obj.listen(5)

def now():
    return time.ctime(time.time())

def handle_client(conn):
    time.sleep(5)
    while True:
        data = conn.recv(1024)
        if not data :
            break
        reply='echo=>%s at %s' % (data,now())
        conn.send(reply.encode())
    conn.close()
def dispatcher():
    while True:
        conn,addr = obj.accept()
        print('server connected by '+ str(addr),end=" ")
        print('at',now())
        threading._start_new_thread(handle_client,(conn,))

dispatcher()

