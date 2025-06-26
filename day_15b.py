# Day 15 of py challenge
# Write a simple TCP client-server application using Python’s socket module.
# Client side

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '172.20.10.3'
PORT = 9999

server.connect((HOST, PORT))
server.send('\nHello,this message is from the client'.encode('utf-8'))
print(server.recv(1024).decode('utf-8'))