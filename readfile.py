# -*- coding: utf-8 -*-
# readfile.py

# ファイルをコピーする
#   このサンプルは、以下の処理の実装例を示しています。
#   - バイナリモードでファイルを読み込んで処理する。
#   - 決まった大きさのデータを読み込みながら、処理をする。
#   - ファイル全体を一度にまとめて読み込み、まとめて書き出す。

# ＜注意＞
# 以下のプログラムのメイン部分（一番最後）は、
# 3つのコピー処理の実体の関数のどれか一つを選択して使うようになっています。
# 一つだけを有効（他はコメントアウトする）にして使って下さい。

import sys 

# 一度に読み書きするデータサイズ[バイト]
CHUNK_SIZE = 4096

# with 構文を使ったファイルの入出力の例
#  with 構文を使ってファイルをオープンすると、
#  ファイルの扱いに伴う例外処理、ファイルのクローズを明示的に書かなくても
#  withのブロックの外側に処理が移ると、ファイルはクローズされます。
def copy_file_with(from_file_name, to_file_name):
    with open(to_file_name, 'wb') as f_out:
        with open(from_file_name, 'rb') as f_in:
            while True:
                data = f_in.read(CHUNK_SIZE)
                if len(data) == 0:
                    break
                f_out.write(data)

# withを使って入出力をするが、
# ファイル全体を一度に読み込んでコピーするバージョン
# 書くのはこちらの方がずっと簡単
# 大きなファイル（何十Mbyteもあるような）を扱うときは、
# それだけメモリも沢山使うので注意
def copy_file_with_at_once(from_file_name, to_file_name):
    with open(to_file_name, 'wb') as f_out:
        with open(from_file_name, 'rb') as f_in:
            data = f_in.read()
            f_out.write(data)

# try〜exceptを使って例外処理をするバージョン
# ファイルの読み書きは CHUNK_SIZEで指定したサイズ単位
def copy_file_try(from_file_name, to_file_name):
    try:
        f_out = open(to_file_name, 'wb')
        f_in = open(from_file_name, 'rb')
        while True:
            data = f_in.read(CHUNK_SIZE)
            if len(data) == 0:
                break
            f_out.write(data)
        f_out.close()
        f_in.close()
    except IOError as e:
        sys.exit(e)   # 例外の情報を表示して終了

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('Usage: {0} from_file_name to_file_name'.format(sys.argv[0]))

    # 注意: copy_file_with, copy_file_with_at_once, copy_file_try
    #       の3つのうちどれか一つだけを有効にして
    #       他の関数はコメントアウトして使うこと

    # with を使ったバージョン
    copy_file_with(sys.argv[1], sys.argv[2])

    # with を使いかつ、一度に読み書きするバージョン
    # copy_file_with_at_once(sys.argv[1], sys.argv[2])

    # tryを使ったバージョン
    # copy_file_try(sys.argv[1], sys.argv[2])
