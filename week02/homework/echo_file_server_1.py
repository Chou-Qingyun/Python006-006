import socket
from pathlib import Path, PurePath, PurePosixPath
import tqdm

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

def receive_file_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"监听: {SERVER_HOST}:{SERVER_PORT}")
    client_socket, addre = s.accept()
    print(f'客户端address：{addre}')
    received = client_socket.recv(BUFFER_SIZE).decode()
    file_name, file_size = received.split(SEPARATOR)
    file_name = PurePosixPath(file_name).name
    file_size = int(file_size)
    # 接受文件
    progress = tqdm.tqdm(range(file_size), f"接收...{file_name}", unit="B", unit_scale=True, unit_divisor=1024)
    file_new_name = Path(__file__).resolve().parent.joinpath('server_file')
    if not file_new_name.is_dir():
        file_new_name.mkdir(mode=0o777)
    file_new_name = Path(file_new_name).joinpath(file_name)
    with open(file_new_name, 'wb') as f:
        for _ in progress:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

    client_socket.close()
    s.close()


if __name__ == '__main__':
    receive_file_server()