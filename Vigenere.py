##################################################################
# Peyton Page
# CYEN 301
# Assignment #2: Vigenere Cipher
#
# 2020-03-21
#
# This program functions correctly using the default 'python'
# command in the Linux Mint terminal.
#
# This program implements a Vigenere Cipher that can encrypt
# or decrypt given text using a given key.
# Exit using Ctrl+D
###################################################################

from sys import stdin, argv
# List of encryptable/decryptable characters
ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# List of characters that can be used in key (case is accounted for in functions)
KEY_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def makeKey(text, key):
	# function to make key be appropriate length
	
	# remove spaces in key
	key = key.replace(" ", "")

	# if key is already appropriate length, return it in uppercase
	if(len(text) == len(key)):
		return key.upper()
	# repeat key until it is same length as given text
	else:
		newKey = key
		for i in range(len(text) - len(key)):
			newKey += key[i % len(key)]

		return newKey.upper()

def encrypt(plaintext, key):
	# function to encrypt plaintext using a given key

	ciphertext = ""
	i = 0
	for c in plaintext:
		# if c is part of the encryptable characters
		if c in ALPHABET:
			# use math and list of encryptable characters to generate the encrypted character
			newChar = (ALPHABET[((ALPHABET.index(c) + KEY_ALPHABET.index(key[i])) % len(ALPHABET))])
			# account for uppercase/lowercase
			if (c.islower()):
				ciphertext += newChar.lower()
			else:
				ciphertext += newChar.upper()
			i += 1
		# if not an encryptable character(" ", "!", ",", etc.) add it to ciphertext
		else:
			ciphertext += c		
		
	return ciphertext

def decrypt(ciphertext, key):
	# function to decrypt ciphertext using a given key
	
	plaintext = ""
	i = 0
	for c in ciphertext:
		# if c is part of the decryptable characters
		if c in ALPHABET:
			# use math and list of decryptable characters to generate the decrypted character
			newChar = (ALPHABET[((len(ALPHABET) + ALPHABET.index(c) - KEY_ALPHABET.index(key[i])) % len(ALPHABET))])
			# account for uppercase/lowercase
			if (c.islower()):
				plaintext += newChar.lower()
			else:
				plaintext += newChar.upper()
			i += 1
		# if not a decryptable character (" ", "!", ",", etc.) add it to plaintext
		else:
			plaintext += c
		
	return plaintext

# test to make sure correct number of arguments are given
if(len(argv) == 3):
	mode = argv[1]
	key = argv[2]
else:
	print("Correct usage is 'python Vigenere.py -e/-d 'some key'")
	exit(0)

# test to make sure mode can only be to encrypt or to decrypt
if(mode != "-e" and mode != "-d"):
	print("mode must be either -e or -d")
	exit(0)

# loop to run until Ctrl+D is pressed
while(1):
	# read line from stdin	
	text = stdin.readline().rstrip("\n")
	
	# make key be appropriate length
	key = makeKey(text, key)

	# encrypt
	if (mode == "-e"):
		ciphertext = encrypt(text, key)
		print(ciphertext)
	# decrypt
	elif(mode == "-d"):
		plaintext = decrypt(text, key)
		print(plaintext)
	# if Ctrl+D is entered, end the program
	if(text == ''):
		break
