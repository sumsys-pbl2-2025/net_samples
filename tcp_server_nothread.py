#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tcp_server_nothread.py for Python 3
#

from socket import *
import time   # for time.sleep()
import threading  # for Thread()

def interact_with_client(s):
    sentence = s.recv(1024).decode()
    print('Received: {0}'.format(sentence))
    time.sleep(15.0)  # wait for 15 seconds 
    capitalized_sentence = sentence.upper()
    print('Sending: {0}'.format(capitalized_sentence))
    s.send(capitalized_sentence.encode())
    s.close()

server_port = 50000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(5)
print('The server is ready to receive')

while True:
    connection_socket, addr = server_socket.accept()
    # スレッドを作らず、単にinteract_with_client()を呼び出し
    interact_with_client(connection_socket)
