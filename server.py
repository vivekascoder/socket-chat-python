import threading
import socket
import time

HOST = "127.0.0.1"
PORT = 8080


def reciever(connection):
    while True:
        data = connection.recv(1024)
        if data:
            print("[CLIENT]: ", data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        recieverThread = threading.Thread(target=reciever, args=(conn, ))
        recieverThread.start()
        print("Connected With: ", addr)
        while True:
            i = input("")
            conn.sendall(bytes(i.encode('utf-8')))
            if i == "q":
                exit()
