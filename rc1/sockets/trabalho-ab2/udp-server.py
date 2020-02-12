import socket

from settings import *

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    while True:
        data, client_addr = s.recvfrom(1024)
        print(f"Connection with {client_addr} established!")
        if not data:
            break
        msg, file_name = data.decode().split("**")
        with open(f"server-folder/{file_name}", "w") as f:
            f.write(msg)
        send_msg = f"File {file_name}, stored!"
        s.sendto(send_msg.encode(), client_addr)
        