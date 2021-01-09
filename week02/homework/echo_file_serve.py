import socket
from pathlib import Path

HOST = "localhost"
PORT = 9000


def echo_file_server():
    """接受文件服务端"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(20)

    while True:
        conn, adder = s.accept()
        print(f'客户端地址：{adder}')
        while True:
            res = conn.recv(1024)
            while res:
                with open('file_bak.txt', 'ab') as f:
                    f.write(res)
                    f.write("\n\r".encode())
                res = conn.recv(1024)
        conn.close()

    s.close()


if __name__ == '__main__':
    echo_file_server()

