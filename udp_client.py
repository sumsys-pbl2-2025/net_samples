# -*- coding: utf-8 -*-
# udp_client.py for Python 3
# トランスポート層にUDPを用いるクライアントプログラム

from socket import *

server_name = 'localhost'
server_port = 50004

# ソケット作成
client_socket = socket(AF_INET, SOCK_DGRAM)   # socket()の第2引数はSOCK_DGRAM

# 送信メッセージ入力
message = input('Input lowercase sentence: ')

# UDPの場合は、connect()をしなくて良い
#  (TCPとは異なりコネクションを作らない）
# サーバ名とポートを指定して、sendto()で送るだけ
client_socket.sendto(message.encode(), (server_name, server_port))

# 受信にはソケットのrecvfrom()を使う
modified_message, server_address = client_socket.recvfrom(2048)

print(modified_message.decode())
client_socket.close()

