#########################################################################################
# Peyton Page 
# CYEN 301
# Assignment #3: FTP (Storage) Covert Channel
#
# 2020-03-30
#
# This program functions correctly using either "python" or "python3"
# command in the Linux Mint terminal. If using "python", the 8-bit encoding
# for FOLDER = "10", METHOD = "10" is unable to convert certain characters
# whose decimal value is between 128 and 255 (converts to "?"), whereas using "python3"
# allows for the extended ascii table (correctly converts to character).
#
# This program connects to a specified FTP site, port, and folder. It takes the contents
# of this folder and extracts and decodes a covert message hidden in the file permissions.
# It has 2 methods. One method uses only the 7 right most bits of the permission and
# filters out any message that does not begin with "---". The other method uses all
# 10 permission bits.
# 
# I have reused the decode function from Program #1 to assist in 
# decoding the coded message.
#########################################################################################

from ftplib import FTP

# Global Variables for FTP Use
IP = "jeangourd.com"
PORT = 21
FOLDER = "7"

# Method selector 
# 7 is for using the 7 right most bits and not using ones that do not start with "---"
# 10 is for using all 10 bits in the permissions
METHOD = 7

# The folder contents
contents = []

# Connect to the specified ftp server and port and save the contents of the specified folder before logging out of the server
ftp = FTP()
ftp.connect(IP,PORT)
ftp.login()
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

# Reusing of decode function from Program #1
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
        
#		move to the next character
		i += n
		

	return text

# Grab only the permissions from each row of contents
permissions = []
for row in contents:
	permissions.append(row[:10])

# Determine what permissions are valid based on the method
# If 7-bit Method check first 3 characters for "---"
# If Method 10 choose entire permissions 
valid = []
for permission in permissions:
	if (permission[:3] == "---" and METHOD == 7):
		valid.append(permission[3:10])
	elif(METHOD == 10):
		valid.append(permission)

# Convert the permissions to binary
binary = ""
text = ""
for string in valid:
	for letter in string:
		if (letter == "-"):
			binary += "0"
		elif (letter == "r" or letter == "w" or letter == "x" or letter == "d"):
			binary += "1"	

# Decode using 7-bit decoding
text = decode(binary, 7)
print(text)

# Based on reccommendation of Dr. Gourd in the video for this program,  
# this additionally decodes the message using 8-bit encoding.
if(METHOD == 10):
	text = decode(binary, 8)
	print(text)


