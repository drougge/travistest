#!/usr/bin/env python

import socket
import time
from threading import Thread

time.sleep(3) # pretend startup is slow

def serve(sock):
	try:
		data = sock.recv(1)
		sock.send(b"%d" % (ord(data),))
	finally:
		sock.close()

listen_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
listen_sock.bind("socket")
listen_sock.listen(5)
while True:
	remote = listen_sock.accept()
	Thread(target=serve, args=(remote[0],)).start()
