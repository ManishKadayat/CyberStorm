##################################################################
# Peyton Page
# CYEN 301
# Assignment #4: Chat (Timing) Covert Channel
#
# 2020-04-17
#
# This program functions requires the use of python 2
#
# This program reads an overt message from a chat server, interprets
# the time between characters, and then gives the covert message.
###################################################################


# import needed libraries and functions
import socket
from sys import stdout, argv
from time import time
from binascii import unhexlify

# Global Variables for checking for delays
ZERO = 0.025
ONE = 0.1

# enables debugging output
DEBUG = False

# set the server's IP address and port
# if not given, default to localhost and 1337
try:
	ip = argv[1]
	port = int(argv[2])
except IndexError:
	ip = "localhost"
	port = 1337

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# initialize covert_bin string for storing the
# covert message as it is received
covert_bin = ""

# receive data until EOF
data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
	# output the overt message
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	# calculate the time delta
	delta = round(t1 - t0, 3)

	# determine if a 1 or a 0 is being sent in the covert message
	if (delta >= ONE):
		covert_bin += "1"
	else:
		covert_bin += "0"

	# Output timings for determining which delay
	# represents a "0" or a "1"
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# initialize a covert string for storing the 
# covert message after converting to ascii
covert = ""

i = 0
while (i < len(covert_bin)):
	# process one byte at a time
	b = covert_bin[i:i + 8]
	# convert it to ASCII
	n = int("0b{}".format(b), 2)
	# if it works, add the character to covert
	try:
		covert += unhexlify("{0:x}".format(n))
	# otherwise, add a "?"
	except TypeError:
		covert += "?"
	# stop at the string "EOF"
	if (covert.endswith("EOF")):
		covert = covert[:-3]
		break

	# move to next byte
	i += 8

# print the covert message
print("Covert message: " + covert)	
# close the connection to the server
s.close()

