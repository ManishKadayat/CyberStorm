################################################################################
# Kevin Ortiz
# Python version 3.8.2
# 3.29.2020
################################################################################

from sys import stdin, argv

index = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text,key):
    cipher = ""
    c = 0
    for i in text:
        if (index.find(i.upper())==-1):
            #print("\n1\n")
            cipher+=i
        elif (i.isupper()):
            #print("\n2\n")
            n = index.find(i)+index.find(key[c].upper())
            n = n%26
            cipher+=index[n]
            if (c==(len(key)-1)):
                c = 0
            else:
                c+=1
        else:
            #print("\n3\n")
            n = index.find(i.upper())+index.find(key[c].upper())
            n = n%26
            cipher+=index[n].lower()
            if (c==(len(key)-1)):
                c = 0
            else:
                c+=1
    return cipher

def decrypt(cipher,key):
    text = ""
    c = 0
    for i in cipher:
        if (index.find(i.upper())==-1):
            #print("\n11\n")
            text+=i
        elif (i.isupper()):
            #print("\n22\n")
            n = index.find(i)-index.find(key[c].upper())
            n = n%26
            text+=index[n]
            if (c==(len(key)-1)):
                c = 0
            else:
                c+=1
        else:
            #print("\n33\n")
            n = index.find(i.upper())-index.find(key[c].upper())
            n = n%26
            text+=index[n].lower()
            if (c==(len(key)-1)):
                c = 0
            else:
                c+=1
    return text

try:
    op = argv[1]
    key = argv[2]

    #print("<Ctrl>+C to exit\n")

    while(True):
        inp = stdin.readline().rstrip("\n")

        if (inp==None or inp==""):
            exit()
        if (op == "-e"):
            print(encrypt(inp,key.replace(" ","")))
        elif (op == "-d"):
            print(decrypt(inp,key.replace(" ","")))
        else:
            print("The only valid operations are -e (encrypt) or -d (decrypt)")
            exit()
        
except IndexError:
    print("Must provide type of operation and key. The only valid operations are -e (encrypt) or -d (decrypt)")

except KeyboardInterrupt:
    print()

