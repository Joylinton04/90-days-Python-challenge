# Day 15 of py challenge
# Write a simple TCP client-server application using Python’s socket module.
# server side

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '172.20.10.3'
PORT = 9999

server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_sock, addr = server.accept()
    print(f"Connected to {addr}")

    message = client_sock.recv(1024).decode('utf-8')
    print(f"The message from the client is: {message}")

    response = "Connection established successfully"
    client_sock.send(response.encode('utf-8'))

    client_sock.close()
    print(f"Connection with {addr} ended!")
