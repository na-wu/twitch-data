# -*- coding: utf-8 -*-

import socket
import logging


# Configure our logs to a specific format #
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log')])



#=== First we define our constants ===#
server = 'irc.chat.twitch.tv' #server client we're connecting to
port = 6667 # port we're going to use
nickname = 'sweetenedyams' # my nickname
token = '' #my twitch authentication token
channel = '#ninja' #Twitch Streamer we are going to be watching




#initialize a socket

sock = socket.socket()


#connect the socket to the server via the port
sock.connect(('irc.chat.twitch.tv', 6667))






#Time to send our token and nickname to the IRC server as encoded strings
#   for authentication
sock.send(u"PASS {token}\n".encode('utf-8'))
sock.send(u"NICK {nickname}\n".encode('utf-8'))
sock.send(u"JOIN {channel}\n".encode('utf-8'))


# Decode and receive the channel message(s)

resp = sock.recv(2048)
logging.info(resp)
    
