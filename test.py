#!/usr/bin/env python

import os
from subprocess import Popen
import socket
import time
import atexit

os.chdir("test")
daemon = Popen(["../daemon.py"])
atexit.register(lambda: os.unlink("socket"))
atexit.register(daemon.terminate)

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
for _ in range(20):
	try:
		sock.connect("socket")
		break
	except Exception: # ...
		if daemon.poll():
			raise Exception("daemon terminated")
		time.sleep(0.5)
else:
	raise Exception("Timed out connecting to daemon")

sock.send(b"a")
print(sock.recv(100))
