import socket

from settings import *

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connection with {addr} established!")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                msg, file_name = data.split("**")
                with open(f"server-folder/{file_name}", "w") as f:
                    f.write(msg)
                send_msg = f"File {file_name}, stored!"
                conn.sendall(send_msg.encode())