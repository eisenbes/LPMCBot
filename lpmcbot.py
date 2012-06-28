import sys
import socket
import string
from botlib import *

HOST = 'irc.freenode.net'       # The server we want to connect to
PORT = 6667                     # The connection port (commonly 6667 for IRC)
NICK = 'LPMCBot'                # The nickname of the bot
USER = 'LPMCbot'                # The username of the bot
REALNAME = 'LPMCBot'            # The real name of the bot
CHANNEL = '#test37283'          # The default channel for the bot
readbuffer = ''                 # Used to store incoming messages from the server

s = socket.socket()             # Create the socket

s.connect((HOST, PORT))         # Connect to the server

# Identify to the server
# Command: USER
# Parameters: <username> <hostname> <servername> <realname>
s.send('USER ' + USER + ' ' + HOST + ' server :' + REALNAME + '\n')

# Give the nickname to the server
# Command: NICK
# Parameters: <nickname> [ <hopcount> ]
s.send('NICK ' + NICK + '\n')

# Infinite listening loop while the bot is in the channel
while True:
    line = s.recv(500)          # Receive a server message (max 500 characters)
    print line                  # Output the server message

# Look for the freenode welcome message
    if 'Welcome to the freenode Internet Relay Chat Network' in line:
# Join the channel
        s.send('JOIN ' + CHANNEL + '\n')

# Handle a private message
    if 'PRIVMSG' in line:
# Use the message parsing function
        send_msg = parsemsg(line)
        s.send(send_msg)
        if send_msg == 'QUIT\n':
            print "QUITTING"
            break

# Handle a PING from the server
    if 'PING' in line:
# Remove the trailing characters
        line = line.rstrip()
# Split the line into an array (using whitespace as a delimiter)
        line = line.split()
# Send back PONG with the correct parameter
        s.send('PONG ' + line[1] + '\n')    
