###################################################################
# Kevin Ortiz
# XOR Cipher
# Python 2
###################################################################
import sys 

def xor(msg, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [msg,key])))

msg=sys.stdin.read()
f=open("key","r")
key=f.read()
f.close()

res=xor(msg,key)
print(res)
