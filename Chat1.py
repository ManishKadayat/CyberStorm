"""
Name: Manish Kadayat
CSC 442-001
Date:4/24/2020
Description: Python program that can extract a covert message.
"""


import socket, sys, re
from time import time
from binascii import unhexlify

# Set defaults
host = '192.168.1.100'
port = 31337
one_time = 0.0
debug = False

# Help information
def help():
    print("IMPORTANT: This is a Python 2 program.\n")
    print("Basic synopsis:\tpython chat.py [host_ip] [-p port_number]")
    print("\nOptions:")
    print("\t-t\tSpecify the minimum time of a 1 bit. \n\t\t\tExample: \"-t 0.05\"\n")
    print("\t-d\tRun in debug mode.\n")
    print("\t-h\tGet helpful information about the program.\n")

# Get parameters
i = 1
while i < len(sys.argv):
    if re.match(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', sys.argv[i]):
        host = sys.argv[i]
        i += 1
    elif sys.argv[i] == '-p':
        port = int(sys.argv[i + 1], 10)
        i += 2
    elif sys.argv[i] == '-t':
        one_time = float(sys.argv[i + 1].strip(''))
        i += 2
    elif sys.argv[i] == '-d':
        debug = True
        i += 1
    elif sys.argv[i] == '-h':
        help()
        exit(0)

if debug:
    print ("Selected host IP: ") + host
    print ("Selected port number: ") + str(port)
    print ("Selected time for '1' bits: ") + str(one_time)

# Establish TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(4096)
covert_bin = ""
covert = ""
times = []

# Get times for covert message
while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()
    t0 = time()
    data = s.recv(4096)
    times.append(round(time() - t0, 5))

# Close the connection once complete
s.close()

if (one_time == 0.0):
    one_time = (sum(times) / len(times))

# Convert times to binary
for time in times:
    covert_bin += "1" if time >= one_time else "0"

# Convert binary to ASCII
i = 0
while i < len(covert_bin):
    b = covert_bin[i : i + 8]
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i += 8

print ("covert")





