
# -*- coding: utf-8 -*-
import socket
import os
import time
a=0
while True:
    print("Connecting...")
    time.sleep(2)
    if os.path.exists("/tmp/python_unix_sockets_example"):
        client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        client.connect("/tmp/python_unix_sockets_example")
        print("Ready.")
        print("Ctrl-C to quit.")
        print("Sending 'DONE' shuts down the server and quits.")
        while True:
            try:
                #client.connect("/tmp/python_unix_sockets_example")
                x = input("> ")
                if "" != x:
                    print("SEND:", x)
                    client.send(x.encode('utf-8'))
                    if "DONE" == x:
                        print("BİTTİ.")
                        break
                    if "end"==x:
                        print("aaaaaa")
                        a=1
                        client.close()
                        break    
            except KeyboardInterrupt as k:
                print("END")
                client.close()
                break
        if a==1:
            break


        if os.path.exists("/tmp/python_unix_sockets_example"):
            os.remove("/tmp/python_unix_sockets_example")
        client.bind("/tmp/python_unix_sockets_example")
        while True:
            datagram = client.recv(1024)
            if not datagram:
                break
            else:
                print("-" * 20)
                print(datagram.decode('utf-8'))
                if "DONE" == datagram.decode('utf-8'):
                    break
                if "end" == datagram.decode('utf-8'):
                    a=2
                    break
        if a==2:
            break     
    else:
        print("Couldn't Connect!")
    print("Done")
    client.close()
