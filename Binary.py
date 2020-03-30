##################################################################
# Peyton Page 
# CYEN 301
# Assignment #1: Binary Decoder
#
# 2020-03-21
#
# This program functions correctly using the default 'python'
# command in the Linux Mint terminal.
#
# This program takes in an encoded 7-bit or 8-bit binary message
# and decodes it using binary-to-ascii decoding.
###################################################################

# Import stdin so that the input can be given using 'python Binary.py < ########' where ### is the input file 
from sys import stdin

def decode(binary, n):
# Decodes various binary encoded messages.
# binary is the given encoded message, which is given in stdin.
# n is the length of each bit.
	text = ""
	i = 0

#	For each character represented by binary, add that character to the returned text
	while ( i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte, 2)
#		If the byte is a backspace, remove the last character in text.
		if (byte == 8):
			text = text[:-1]
#		If the byte is a tab, add a tab instead of simply moving the cursor.
		elif (byte == 9):
			text += "\t"
#		Otherwise just add the character to text
		else:
			text += chr(byte)
        
##		move to the next character
		i += n

	return text

# read given binary from stdin
binary = stdin.read().rstrip("\n")

# for 7-bit binary
if (len(binary) % 7 == 0):
	text = decode(binary, 7)
# for 8-bit binary
elif (len(binary) % 8 == 0):
	text = decode(binary, 8)

# print the resulting text
print(text)
