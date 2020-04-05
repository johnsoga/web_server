#!/bin/python

import socket
import sys

host = '127.0.0.1'
port = 50000

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()

    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            break
        conn.sendall(data)
        s.close()

except:
    print("Something Happened")
