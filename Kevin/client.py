import socket
from sys import stdout
from time import time


#Binary Decoder
def Decoder(msg):
    res1=''
    for n in range(int(len(str(msg))/7)):
        res1+=chr(int(msg[0+n*7:7+n*7],2))

    res2=''
    for n in range(int(len(msg)/8)):
        res2+=chr(int(msg[0+n*8:8+n*8],2))

    return res1,res2


# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.102.67"
port = 33333

#Covert delays
ZERO = 0.1
ONE = 0.2

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
msg=''
while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
	# start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096)
    t1 = time()
	# calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 1)
    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

    #Get binary msg
    if (delta==ZERO):
        msg+='0'
    elif (delta==ONE):
        msg+='1'

# close the connection to the server
s.close()

#Covert msg
msg7, msg8 = Decoder(msg)
print("\nDecoded as 7-bit: "+msg7)
print("\nDecoded as 8-bit: "+msg8)

