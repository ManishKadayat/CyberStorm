import socket
from time import sleep
from binascii import hexlify
from sys import stdout


ZERO = 0.025
ONE = 0.1



delay_mode = 0

def cycleServerPort(s, port):
	try:
		s.bind(("", port))
	except socket.error:
		cycleServerPort(s, port+1)
# set the port for client connections
port = 1337

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cycleServerPort(s, port)

# listen for clients
# this is a blocking call
s.listen(0)

# a client has connected!
c, addr = s.accept()

# set the message
msg = "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, but when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new Avatar, an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. But I believe Aang can save the world.\n"

covert = "Louisiana Tech University" + "EOF"

covert_bin = ""
for i in covert:
	# convert each character to a full byte
	# hexlify converts ASCII to hex
	# int converts the hex to a decimal integer
	# bin provides its binary representation (with a 0b
	# prefix that must be removed)
	# that's the [2:] (return the string from the third
	# character on)
	# zfill left-pads the bit string with 0s to ensure a
	# full byte
	covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

n = 0

# send the message, one letter at a time
for i in msg:
	c.send(i)
	if (covert_bin[n] == "0"):
		sleep(ZERO)
	elif (covert_bin[n] == "1"):
		sleep(ONE)

	n = (n + 1) % len(covert_bin)

#print(covert_bin)


c.send("EOF")
c.close()

