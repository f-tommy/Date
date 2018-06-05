#!/usr/bin/env python3
# This script transform date to GPSweek,days,hours,minites,seconds
import fileinput
import math
from datetime import datetime, date, time

ref = datetime.strptime('1980/01/06 00:00:00', '%Y/%m/%d %H:%M:%S')
siw = 3600*24*7  # secounds in a week
sid = 3600*24  # secounds in a day
sih = 3600  # secounds in a hour
sim = 60  # secounds in a minite
for line in fileinput.input():
 lin = line.rstrip('\n')
 col = lin.split()
 dat1 = ' '.join(col[0:2]) # list to string
 dat2 = ' '.join(col[2:]) # list to string
# org = datetime.strptime(line.rstrip('\n'), '%Y/%m/%d %H:%M:%S')
 org = datetime.strptime(dat1, '%Y/%m/%d %H:%M:%S')
 ds = org.timestamp() - ref.timestamp() # timestamp is function calculating UNIX time
 gw = math.floor( ds / siw )
 dw = ds % siw
 gd = math.floor( dw / sid )
 dd = dw % sid
 gh = math.floor( dd / sih )
 dh = dd % sih
 gm = math.floor( dh / sim )
 dm = dh % sim
 print(gw,gd,gh,gm,dm,dat2)
