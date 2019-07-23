# -*- coding: utf-8 -*-
import socket
import os
import time

if os.path.exists("/tmp/python_unix_sockets_example"):
    os.remove("/tmp/python_unix_sockets_example")

print("Opening socket...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind("/tmp/python_unix_sockets_example")

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print("-" * 20)
        print(datagram.decode('utf-8'))
        if "DONE" == datagram.decode('utf-8'):
            break
time.sleep(3)
server.connect("/tmp/python_unix_sockets_example")
while True:
    try:
       #server.connect("/tmp/python_unix_sockets_example")
       x = input("> ")
       if "" != x:
            print("Send:", x)
            server.send(x.encode('utf-8'))
            if "DONE" == x:
               print("Shutting Down")
               break
    except KeyboardInterrupt as k:
        print("Shutting down.")
        break

print("-" * 20)
print("Shutting down...")
server.close()
os.remove("/tmp/python_unix_sockets_example")
print("Done")