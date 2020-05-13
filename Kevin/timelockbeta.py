from datetime import timedelta
from datetime import datetime
from hashlib import md5
import hashlib

letters=""
numbers=""
DEBUG=True
Daylight=False
epoch="1999 12 31 23 59 59"

#epoch="2000 01 01 05 59 59"

#current="2013 05 06 12 43 25"
    

epoch=epoch.split(" ")
current=current.split(" ")

epoch = list(map(int, epoch))
current = list(map(int, current))



epoch_time=datetime(year=epoch[0],month=epoch[1],day=epoch[2],hour=epoch[3],minute=epoch[4],second=epoch[5])

      
current_time=datetime(year=current[0],month=current[1],day=current[2],hour=current[3],minute=current[4],second=current[5])
current_time=datetime.now()

if (DEBUG):
      print(epoch_time)
      print(current_time)
      
delta_time=abs(current_time-epoch_time)
delta_time=delta_time.total_seconds()


if (Daylight):
      delta_time=delta_time-(21600.0)

print(delta_time)
delta_time=int(delta_time-(delta_time%60))
print(delta_time)

result=md5(str(md5(str(delta_time).encode("ascii")).hexdigest()).encode("ascii")).hexdigest()

for character in result:
      if (character.isdigit()):
            numbers=numbers+character
      else:
            letters=letters+character
print(letters[0:2]+numbers[-1]+numbers[-2])


