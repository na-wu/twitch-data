# -*- coding: utf-8 -*-

import socket
import logging

import config
# Configure our logs to a specific format #
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log')])

#=== First we define our constants ===#
HOST = config.server #HOST client we're connecting to
PORT = 6667 # port we're going to use
NICKNAME = config.nickname #NICKNAME
TOKEN = config.token #twitch authentication TOKEN
CHANNEL = config.channel #Twitch Streamer we are going to be watching

#initialize a socket
sock = socket.socket()
#connect the socket to the HOST via PORT 6667
sock.connect((HOST, PORT))
#Send TOKEN and NICKNAME to the IRC HOST as encoded strings
#   for authentication
sock.send(f"PASS {TOKEN}\n".encode('utf-8'))
sock.send(f"NICK {NICKNAME}\n".encode('utf-8'))
sock.send(f"JOIN {CHANNEL}\n".encode('utf-8'))


# Decode and receive the CHANNEL message(s)
while True:
    resp = sock.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        print(resp)
        logging.info(resp)
        sock.close()
    print(resp)
    logging.info(resp)


sock.close()


