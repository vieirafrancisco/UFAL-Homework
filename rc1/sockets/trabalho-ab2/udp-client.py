import sys
import socket

from settings import *

file_name = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    with open(f"client-folder/{file_name}", "r") as f:
        txt = ''
        for line in f.readlines():
            txt += line
        txt += f'**{file_name}'
    s.sendto(txt.encode(), (HOST, PORT))
    result_msg = s.recv(1024)

print(result_msg.decode())