# net_samples

このリポジトリには、ネットワークプログラミング学習のためのサンプルプログラムが格納されています。

## 第4回 演習2: TCPによる通信プログラム
    - tcp_server.py
    - tcp_client.py

## 第4回 演習3: ファイル転送プログラム〜大きなデータの送受信
    - filetrans_server.py
    - filetrans_client.py

## 第4回 補足資料: 大きなファイルをバイナリモードで読み書きする方法について
    - readfile.py

    - 参考ランダムなバイナリファイルを作る方法（例 1MBのランダムバイナリファイルを作る）
    `head -c 1M /dev/urandom > random_file.bin`

    - 参考ランダムなテキストファイルを作る方法（例 1kBのランダムテキストファイルを作る）
    `tr -dc '0-9a-zA-Z' < /dev/urandom | head -c 1024 > random_text.txt

## 第5回 演習1: マルチスレッドを使ったサーバプログラム/UDPの通信/時間計測
    - tcp_server_thread.py
    - tcp_server_nothread.py
    - udp_server.py
    - udp_client.py
    - time_test.py

