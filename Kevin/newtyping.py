from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

sleep(3)

password = raw_input()
timings = raw_input()

#print "password = {}".format(password)
#print "timings = {}".format(timings)

password = password.split(",")
password = password[:len(password) / 2 + 1]
password = "".join(password)

#print password

timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings) / 2 + 1]
keyintervals = timings[len(timings) / 2 + 1 :]

#print "Keypress times = {}".format(keypress)
#print "Keyinterval times = {}".format(keyintervals)


keyboard = Controller()

#string = "this is a really long string that someone is typing out"
n = 0
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(6)
for char in password:
    #keyboard.press(Key.enter)
    keyboard.press(char)
    sleep(keypress[n])
    keyboard.release(char)
    if ((len(password)-1) == (n)):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        sleep(keyintervals[n])
    n = n+1


#tcflush(stdin, TCIFLUSH)
print 
