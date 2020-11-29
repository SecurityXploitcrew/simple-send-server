#coding by Tegar sxc
#team SecurityXploitcrew and tkj blackhats

import os
import socket
import sys

ip = '127.0.0.1'
port = 8080
size = 10
pesan = "its me tegar sxc \n"

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((ip, port))

tcp_socket.send(bytes(pesan.encode("UTF-8")))
