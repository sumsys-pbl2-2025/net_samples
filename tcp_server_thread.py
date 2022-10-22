#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tcp_server_thread.py for Python 3
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

    # スレッドを作り、そこで動かす関数と引数をスレッドに与える
    #   argsに与えるのはタプル(xxx, xxx, ...)でないといけないので、
    #   たとえ引数が一つであっても、括弧で囲い、かつ、ひとつめの要素のあとにカンマを入れる。
    client_handler = threading.Thread(target=interact_with_client, args=(connection_socket,))
    client_handler.start()  # スレッドを開始
