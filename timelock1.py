"""
Name: Manish Kadayat
Program: Timelock
Date: 5/8/2020
"""

import sys, datetime, hashlib

# Initialize variables
debug = False
e_arr = []
now_arr = []

def help():
    print("IMPORTANT: This is a Python 3 program.\n")
    print("IMPORTANT: Must echo in the epoch time (see basic synopsis).\n")
    print("Basic synopsis:\techo \"YYYY MM DD HH mm SS\" | python3 timelock.py [-d] [-t current_sys_time]")
    print("\nOptions:")
    print("\t-d\tRun in debug mode.\n")
    print("\t-t\tSpecify current system time to use. \n\t\t\tExample: \"-t 2017 01 01 00 00 00\"\n")
    print("\t-h\tGet helpful information about the program.\n")

# If -d param is provided, run in debug mode
i = 1
while i < len(sys.argv):
    if sys.argv[i] == '-d':
        debug = True
        i += 1
    elif sys.argv[i] == '-t':
        now_arr = list(map(int, sys.argv[i+1:i+7]))
        i += 8
    elif sys.argv[i] == '-h':
        help()
        exit(0)
    else:
        i += 1

# Get epoch date/time string from stdin
e_arr = list(map(int, str(sys.stdin.read()).strip().split(" ")))

# Debug statement
if debug:
    print("Tokenized epoch: %s" % str(e_arr))
    print("Tokenized system time (if provided): %s\n" % str(now_arr))

# Create datetime objects for epoch and current date/time
epoch = datetime.datetime(e_arr[0], e_arr[1], e_arr[2], e_arr[3], e_arr[4], e_arr[5], 0)
epoch.replace(microsecond = 0)
epoch = datetime.datetime.utcfromtimestamp(epoch.timestamp())

if len(now_arr) == 6:
    now = datetime.datetime(now_arr[0], now_arr[1], now_arr[2], now_arr[3], now_arr[4], now_arr[5], 0)
    now.replace(microsecond = 0)
    now = datetime.datetime.utcfromtimestamp(now.timestamp())
else:
    now = datetime.datetime.now()
    now.replace(microsecond = 0)
    now = datetime.datetime.utcfromtimestamp(now.timestamp())

sec_diff = int((now - epoch).total_seconds() - ((now - epoch).total_seconds() % 60))

# Debug statement
if debug:
    print("Epoch datetime: %s" % str(epoch))
    print("Now datetime: %s\n" % str(now))
    print("Difference (now - epoch): %i\n" % sec_diff)

# Calculate and print the double-hash of the time difference
diff_hash = list(hashlib.md5(str(hashlib.md5(str(sec_diff).encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest())

if debug:
    print(diff_hash)

result = ""

index = 0
while index < len(diff_hash):
    if diff_hash[index].isalpha():
        result += diff_hash[index]
        diff_hash.pop(index)

        if len(result) > 1:
            break
    else:
        index += 1

index = len(diff_hash) - 1
while index >= 0:
    if diff_hash[index].isnumeric():
        result += diff_hash[index]
        if len(result) > 3:
            break
    index -= 1

if len(result) < 4:
    for ch in diff_hash:
        if ch.isalpha():
            result += ch
        if len(result) > 3:
            break

print(result)
