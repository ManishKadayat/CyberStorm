# Peyton Page
# 
# 5/3/2020
#
# Assignment #6: XOR Crypto
# 
# This code takes in a ciphertext or a plaintext binary data message
# and binary xor's it with a key. The key is located in a file named "key"
# in the same directory as the python file. 
#
# python3 is used for this assignment.
#
# This code could be improved by adding functionality to account for 
# a situation where the key is not the same size as the message.

# Import stdin and stdout
from sys import stdin, stdout

# Global Variable for changing name of key file (For testing purposes)
KEY_FILE = "key"

# Read the key file as binary data
key = bytearray(open(KEY_FILE, "rb").read())

# Read the message from stdin as binary data
message = bytearray(stdin.buffer.read())

# Generate the resulting binary data.
# For each item in key and message, xor them and
# return the bytes version of that xor result.
result = bytes(k ^ m for k,m in zip(key, message))

# Write the result to stdout.buffer
stdout.buffer.write(result)


