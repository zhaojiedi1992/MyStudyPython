from socket import *
host=''
port=50007

with socket(family=AF_INET,type=SOCK_STREAM) as s:     
    s.bind((host,port))
    s.listen(5)
    conn,addr = s.accept()
    with conn:
        print("connected by ",addr)
        while True:
            data = conn.recv(1024)
            if not data:break
            conn.sendall(data +b"XXXX")
