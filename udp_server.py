# -*- coding: utf-8 -*-
# udp_server.py for Python 3
# トランスポート層にUDPを用いるサーバプログラム

from socket import *

server_port = 50004

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('The server is ready to receive.')

# UDPを使う場合は、listen(), accept()は使用しない

while True:
    # recvfrom()で受信。受信データとクライアントアドレスのタプルが戻り値
    message, client_address = server_socket.recvfrom(2048)

    # 受信した文字列を大文字に変換して返送する
    modified_message = message.decode().upper()

    # sendto()で送信 明示的に相手のアドレスとポートを指定
    #  ここでのclient_addressはホスト名とポート番号のタプルになっている
    server_socket.sendto(modified_message.encode(), client_address)
