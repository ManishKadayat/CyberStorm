"""
Name: Manish Kadayat
CSC 442-001
Description: Program that can decode various binary encoded messages.
Date: 3/30/2020
"""

import os
import sys


#if no file is specified:
if len(sys.argv) == 1:
    print ("Enter some binary numbers: ")
    Data = sys.stdin.readline()


else:
    test_file = open(sys.argv[1], 'rb')
    Data = test_file.read()

Data = Data[:-1]
#if we divide/separate the binary integers in files into group of 8s, only one of them prints the correct message
#for the rest of the files provided, groups of 7s work.

n = 7

if len(Data) % 8 == 0:
    n = 8

groups = []

result =[]

while Data:

    #adds the group of
    groups.append(Data[:n])

    Data = Data[n:]

print(groups)

j = 0 #len(groups)-1

while j < len(groups):

    #this is where the conversion to text characters takes place.
    convert = int((groups[j]), 2)

    j += 1

    result.append(convert)

print(''.join(map(chr,result)))

