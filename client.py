import threading
import socket
import time

HOST = "127.0.0.1"
PORT = 8080


def reciever(connection):
    while True:
        data = connection.recv(1024)
        if data:
            print("[ADMIN]: ", data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    recieverThread = threading.Thread(target=reciever, args=(s,))
    recieverThread.start()
    while True:
        i = input("")
        s.sendall(bytes(i.encode('utf-8')))
        if i == "q":
            exit()
