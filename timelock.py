# Peyton Page
# 
# 5/5/2020
#
# Assignment #5: TimeLock
# 
# This code takes an epoch time from stdin and determines the seconds elapsed
# between now and then. It then double hashes these seconds and creates a 
# code using the first two letters and the last two number (reversed order)
# in the second hash. 
#
# python3 is used for this assignment.
#
# This code could be improved by adding functionality to account for if the 
# second time hash does not contain 2 letters or 2 numbers

# Import needed libraries
from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5

# Toggle Debug Mode
DEBUG = False
# Interval on which hashes are changed
INTERVAL = 60
# Set the timezone, used for epoch time and manually entered times
TIMEZONE = "America/Chicago"

# Manually set the current time 
MANUAL_DATETIME = ""#2017 04 26 15 14 30"
# Get the Epoch time from stdin
EPOCH_TIME = stdin.readline().rstrip("\n")

# Function for converting a time to UTC Timezone
def timeToUTC(timezone, time):
	local = pytz.timezone(timezone)
	time_dt = local.localize(time, is_dst=False)
	time_utc = time_dt.astimezone(pytz.utc)

	return time_utc

# If I manually give a current time, now is that time
if(MANUAL_DATETIME != ""):
	now = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
else:
	# otherwise, now is the current system time in UTC Timezone
	now = datetime.now()

now = timeToUTC(TIMEZONE, now)

epoch = datetime.strptime(EPOCH_TIME, "%Y %m %d %H %M %S")
epoch = timeToUTC(TIMEZONE, epoch)


# Create time elapsed
time_elapsed = int(((now - epoch).total_seconds()))
# Only hash on a predefined interval
time_elapsed_interval = (time_elapsed // INTERVAL) * INTERVAL

# Hash the seconds elapsed twice
MD5num1 = md5(str(time_elapsed_interval).encode()).hexdigest()
MD5num2 = md5(str(MD5num1).encode()).hexdigest()

# Create the code
numNums = 0
numChars = 0
code = ""
# Get the first two letters
for c in MD5num2:
	if c.isalpha():
		code += c
		numChars += 1
	if (numChars == 2):
		break
# Get the last two numbers in reverse order
for n in MD5num2[::-1]:
	if n.isdigit():
		code += n
		numNums += 1
	if (numNums == 2):
		break

# Print extra info if needed
if(DEBUG):
	print(f"Current (UTC): {now}")
	print(f"Epoch (UTC): {epoch}")
	print(f"Seconds: {time_elapsed}")
	print(f"Seconds: {time_elapsed_interval}")
	print(f"MD5#1: {MD5num1}")
	print(f"MD5#2: {MD5num2}")
	print(f"code: {code}")
else:
	# Print just the code
	print(code)
