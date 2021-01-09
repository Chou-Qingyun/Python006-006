import socket

HOST = 'localhost'
PORT = 9000

def echo_file_client():
    """客户端发送文件"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    try:
        with open("file_content.txt", 'rb') as f:
            content = f.read()
            s.sendall(content)

    except FileNotFoundError as e:
        print(f'文件不存在：{e}')

    s.close()


if __name__ == "__main__":
    echo_file_client()