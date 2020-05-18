"""
Name: Manish Kadayat
CSC 442-001
Description: Program that mathematically implements the Vigenere Cipher.
Date: 3/30/2020
"""

import sys
import fileinput


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rotKey = []

def shiftChar(c, n):
    try:
        if c.islower() == True:
            flag = True
            c = c.upper()
        else:
            flag = False
        i = alphabet.index(c) 
        i = i + n 
        i = i % len(alphabet)
        if flag == True:
            return alphabet[i].lower()
        else:
            return alphabet[i]
    except ValueError:
        return c

def setupRotKey(k):
    k = k.upper()
    k = "".join(k.split())
    for char in k:
        rotKey.append(alphabet.index(char))


def vEnc(str, k):
    setupRotKey(k)
    limit = len(rotKey)
    i = 1
    cTxt = []
    for word in str:
        for letter in word:
            try:
                alphabet.index(''.join(letter.upper()))
                cTxt.append(shiftChar(letter, rotKey[i-1]))
                if (i%limit == 0):
                    i = 1
                else:
                    i = i + 1
            except ValueError:
                cTxt.append(letter)
    return ''.join(cTxt)

def vDec(str, k):
    setupRotKey(k)
    limit = len(rotKey)
    i = 1
    pTxt = []
    for word in str:
        for letter in word:
            try:
                alphabet.index(''.join(letter.upper()))
                pTxt.append(shiftChar(letter, (rotKey[i-1]*-1)))
                if (i%limit == 0):
                    i = 1
                else:
                    i = i + 1
            except ValueError:
                pTxt.append(letter)
    return ''.join(pTxt)

    
while True:
    flag = False 
    if not sys.stdin.isatty():
        msg = sys.stdin.read()
        flag = True
    else:
        msg = raw_input()
        
    key = sys.argv[2:]
    key = ''.join(key)
    if (sys.argv[1] == '-e'):
        print (vEnc(msg, key))
    elif (sys.argv[1] == '-d'):
        print (vDec(msg, key))
        
    if (flag == True):
        break
        
