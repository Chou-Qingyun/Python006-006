import socket
from pathlib import Path
import tqdm

host = '127.0.0.1'
port = 5000

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096  # 每次发送4096字节

file_name = 'runapi-1.0.0.zip'


def send_file_client(file_name='file_content.txt'):
    p = Path(file_name)
    if p.exists():
        file_size = p.stat().st_size
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"链接...{host}:{port}")
        s.connect((host, port))
        print("已连接")
        s.send(f"{file_name}{SEPARATOR}{file_size}".encode())
        progress = tqdm.tqdm(range(file_size), f"发送 {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(file_name, "rb") as f:
            for _ in progress:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))
        # 关闭连接
        s.close()


if __name__ == '__main__':
    send_file_client(file_name)