#!/usr/bin/env python3
# echo "year cal" | cal2wtime.py
import fileinput
import math
from datetime import datetime, date, timedelta

ref0 = datetime.strptime('1980/01/06 00:00:00', '%Y/%m/%d %H:%M:%S')
siw = 3600*24*7  # secounds in a week
sid = 3600*24  # secounds in a day
sih = 3600  # secounds in a hour
sim = 60  # secounds in a minite
for line in fileinput.input():
 lin = line.rstrip('\n')
 col = lin.split()
 ref = datetime.strptime(str(col[0]),"%Y") # Year
 dat1 = int(col[1]) - 1 # Cal
 dat2 = ' '.join(col[2:]) # list to string
 dat = ref + timedelta(days=dat1)
 ds = dat.timestamp() - ref0.timestamp() 
 gw = math.floor( ds / siw )
 dw = ds % siw
 gd = math.floor( dw / sid )
 print(gw,gd,dat2)
