password = raw_input()
timings = raw_input()

print "password = {}".format(password)
print "timings = {}".format(timings)

password = password.split(",")
password = password[:len(password) / 2 + 1]
password = "".join(password)

print password

timings = timings.split(",")
timings = [float(a) for a in timings]
keypress = timings[:len(timings) / 2 + 1]
keyintervals = timings[len(timings) / 2 + 1 :]

print "Keypress times = {}".format(keypress)
print "Keyinterval times = {}".format(keyintervals)
