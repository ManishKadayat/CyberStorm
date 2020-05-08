# Peyton Page
# 
# 5/7/2020
#
# Assignment #6: Steg
# 
# This code has the ability to both store and retrieve hidden data into or from
# a wrapper file using either a bit or byte method 
#
# python3 is used for this assignment.
#

# Import needed libraries
from sys import stdin, stdout, argv

# Debug mode
DEBUG = False

# Create variables for the parameters to be stored in
MODE = ""
METHOD = ""
OFFSET = ""
INTERVAL = ""
WRAPPER_FILE = ""
HIDDEN_FILE = ""

# Sentinel
SENTINEL = bytearray(b'\x00\xff\x00\x00\xff\x00')

# for determining if offset or interval have not been given
OFFSET_DEFAULT = 0
INTERVAL_DEFAULT = 0

# for giving an error when parameters are not valid
INVALID_PARAMETERS = False

# Interpret parameters from argv
try:
	if (argv[1] == "-s"):
		MODE = "store"
	elif (argv[1] == "-r"):
		MODE = "retrieve"
	else:
		INVALID_PARAMETERS = True
	if (argv[2] == "-b"):
		METHOD = "bit"
	elif (argv[2] == "-B"):
		METHOD = "byte"
	else:
		INVALID_PARAMETERS = True

	if (argv[3][:2] == "-o" and argv[3][2:]):
		OFFSET = int(argv[3][2:])
	else:
		OFFSET = 0
		OFFSET_DEFAULT = 1

	if (argv[4 - OFFSET_DEFAULT][:2] == "-i" and argv[4 - OFFSET_DEFAULT][2:]):
		INTERVAL = int(argv[4][2:])
	else:
		INTERVAL = 1
		INTERVAL_DEFAULT = 1

	if (argv[5 - OFFSET_DEFAULT - INTERVAL_DEFAULT][:2] == "-w" and argv[5 - OFFSET_DEFAULT - INTERVAL_DEFAULT][:2]):
		WRAPPER_FILE = argv[5 - OFFSET_DEFAULT - INTERVAL_DEFAULT][2:]
	else:
		INVALID_PARAMETERS = True

	if (MODE == "retrieve"):
		pass
	else:
		if (argv[6 - OFFSET_DEFAULT - INTERVAL_DEFAULT][:2] == "-h" and argv[6 - OFFSET_DEFAULT - INTERVAL_DEFAULT][:2]):
			HIDDEN_FILE = argv[6 - OFFSET_DEFAULT - INTERVAL_DEFAULT][2:]
		else:
			INVALID_PARAMETERS = True
except IndexError:
	INVALID_PARAMETERS = True


# Print more info
if (DEBUG):
	print(f"Mode: {MODE}")
	print(f"Method: {METHOD}")
	print(f"Offset: {OFFSET}")
	print(f"Interval: {INTERVAL}")
	print(f"Wrapper File: {WRAPPER_FILE}")
	if(MODE == "retrieve"):
		pass
	else:
		print(f"Hidden File: {HIDDEN_FILE}")

# Print valid usage
if (INVALID_PARAMETERS):
		print("Proper usage is : python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]\n\
		  -s store\n\
		  -r retrieve\n\
		  -b bit mode\n\
		  -B byte mode\n\
		  -o<val> set offset to <val> (default is 0)\n\
		  -i<val> set interval to <val> (default is 1)\n\
		  -w<val> set wrapper file to <val>\n\
		  -h<val> set hidden file to <val>")


# function that implements the algorithm to store
# in byte mode
def storeByte(W, H, offset, interval):

	for i in range(len(H) - 1):
		W[offset] = H[i]
		offset += interval

	for j in range(len(SENTINEL) - 1):
		W[offset] = SENTINEL[j]
		offset += interval

	return W

# function that retrieves in byte mode
def retrieveByte(W, H, offset, interval):

	while(offset < len(W)):
		b = W[offset]

		if b in SENTINEL:
			for i in range(1, len(SENTINEL)):
				if (W[offset:offset + (interval * len(SENTINEL)): interval] == SENTINEL):
					return H
		
		H.append(b)
		offset += interval

# stores in bit mode
# Note that there is currently an issue involving new lines in the hidden file
def storeBit(W, H, offset, interval):

	for i in range(len(H) - 1):
		for j in range(8):
			W[offset] &= 0xfe
			W[offset] |= ((H[i] & 0x80) >> 7)
			H[i] = (H[i] << 1) & (2 ** 8 - 1)
			offset += interval
		i+=1

	for i in range(len(SENTINEL) - 1):
		for j in range(8):
			W[offset] &= 0xfe
			W[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
			SENTINEL[i] = ((SENTINEL[i] << 1) & (0b11111111))
			offset += interval

	return W

# retrieves in bit mode
def retrieveBit(W, H, offset, interval):
	found = False
	sentinel_array = bytearray()
	while(offset < len(W) - 8*interval):
		b = 0

		for j in range(8):
			b |= (W[offset] & 0x01)
			if (j < 7):
				b = (b << 1) & (0xff)
				offset += interval

		if (b in SENTINEL):
			sentinel_array.append(b)
		else:
			sentinel_array = bytearray()

		if (sentinel_array == SENTINEL):
			H = H[0:len(H) - len(SENTINEL) + 1]
			return H

		H.append(b)
		offset += interval

# open the wrapper and hidden files and save as bytearray
WRAPPER = open(WRAPPER_FILE, "rb").read()
W = bytearray(WRAPPER)

if(HIDDEN_FILE):
	HIDDEN = open(HIDDEN_FILE, "rb").read()
	H = bytearray(HIDDEN)
else:
	H = bytearray()



# Determine which mode and method to use.
# Write the result to stdout.buffer
if(MODE == "store" and METHOD == "byte"):
	stdout.buffer.write(storeByte(W, H, OFFSET, INTERVAL))

if(MODE == "retrieve" and METHOD == "byte"):
	stdout.buffer.write(retrieveByte(W, H, OFFSET, INTERVAL))

if(MODE == "store" and METHOD == "bit"):
	stdout.buffer.write(storeBit(W, H, OFFSET, INTERVAL))

if(MODE == "retrieve" and METHOD == "bit"):
	stdout.buffer.write(retrieveBit(W, H, OFFSET, INTERVAL))


stdout.flush()


