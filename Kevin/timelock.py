from datetime import timedelta,datetime
from hashlib import md5
import hashlib
from sys import stdin

letters=""
numbers=""
DEBUG=False
TEST=False
CT="2015 01 01 00 01 30"
Daylight=False
epoch=stdin.read()


epoch=epoch.split(" ")
epoch=list(map(int,epoch))
epoch_time=datetime(year=epoch[0],month=epoch[1],day=epoch[2],hour=epoch[3],minute=epoch[4],second=epoch[5])

if (TEST):
    current=CT
    current=current.split(" ")
    current=list(map(int,current))
    current_time=datetime(year=current[0],month=current[1],day=current[2],hour=current[3],minute=current[4],second=current[5])
else:
    current_time=datetime.now()

if (DEBUG):
      print(epoch_time)
      print(current_time)
      
delta_time=abs(current_time-epoch_time)
delta_time=delta_time.total_seconds()


if (Daylight):
      delta_time=delta_time-(21600.0)

if (DEBUG):
    print(delta_time)
delta_time=int(delta_time-(delta_time%60))
if (DEBUG):
    print(delta_time)

result=md5(str(md5(str(delta_time).encode("ascii")).hexdigest()).encode("ascii")).hexdigest()

for character in result:
      if (character.isdigit()):
            numbers=numbers+character
      else:
            letters=letters+character
print(letters[0:2]+numbers[-1]+numbers[-2])
