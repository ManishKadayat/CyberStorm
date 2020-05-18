import sys 

'''
Name: Manish Kadayat
Date: 5/8/2020
Description: This program will encrypt any file from stdin with a file named 'key' in the same directory as this script. The resultant is sent to stdout. 
Note: This program works on Python3.
'''

if(sys.argv[1] == '-h'):
    print ('PYTHON3 REQUIRED PYTHON3 REQUIRED PYTHON3 REQUIRED')
    print ('This program will encrypt and decrypt files PROVIDED A KEY OF EQUAL SIZE.')
    print ('This program only takes input from stdin and only outputs to stdout.')
    print ('The key file must always be the 1st argument, the key is always req.')
    print ('HINT: if you need a random key, with the same size as your file, copy paste the file. ez keyz.')
    print ('  Exmaple Usage:  xor key.book < t-rex.xyz > encrypted_t-rex.pls ')
    print ('  Exmaple Usage:  xor yo.key < enc_hardware.ram > freeram.ram ')
    sys.exit()

key = sys.argv[1]
keyFile = open(key, 'rb')     # 'rb' -> Allows reading of bytes

inBytes = b''
keyBytes = b''

# Example buffer used for performance.
BUFFER_SIZE = 4096

# Reading from the buffer skips around python trying to
# interpret everything and reads just bytes
inBytes = sys.stdin.buffer.read(BUFFER_SIZE) 
keyBytes = keyFile.read(BUFFER_SIZE)

# Will encrypt the entire length of stdin to stdout. 
while len(inBytes) > 0 :                                # Grabs 1 to 4096 bytes
        for i in range(0, len(inBytes)):                # For each byte grabbed, xor it with key            
            xord = bytes([inBytes[i] ^ keyBytes[i]])    # XOR operation between 2 bytes
            sys.stdout.buffer.write(xord)               # Writting to buffer allows the writing of bytes.
        inBytes = sys.stdin.buffer.read(BUFFER_SIZE) 
        keyBytes = keyFile.read(BUFFER_SIZE)
