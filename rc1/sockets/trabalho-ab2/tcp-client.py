import sys
import socket

from settings import *

file_name = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open(f"client-folder/{file_name}", "r") as f:
        txt = ''
        for line in f.readlines():
            txt += line
        txt += f'**{file_name}'
    s.sendall(txt.encode())
    result_msg = s.recv(1024)

print(result_msg.decode())