###############################################
# Kevin Ortiz
# Python version 3.8.2
# 3.29.2020
###############################################

msg=input()
print(msg)
msg=str(msg)
print(msg)

res1=''
for n in range(int(len(str(msg))/7)):
    res1+=chr(int(msg[0+n*7:7+n*7],2))
print("\nDecoded as 7-bit: "+res1)

res2=''
for n in range(int(len(msg)/8)):
    res2+=chr(int(msg[0+n*8:8+n*8],2))
print("Decoded as 8-bit: "+res2)
