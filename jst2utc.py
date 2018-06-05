#!/usr/bin/env python3
# echo "yyyy/mm/dd hh:mm:ss" | jst2utc.py
# Transform time zone: jst2utc
import fileinput
from datetime import datetime
from datetime import timedelta

# Process line input
for line in fileinput.input():
    lin = line.rstrip('\n')
    col = lin.split()
    date1 = datetime.strptime(' '.join(col[0:2]),"%Y/%m/%d %H:%M:%S")
    date2 = date1 + timedelta(hours=-9)
    tmp1 = ' '.join(col[2:]) # list to string
    print(date2.strftime("%Y/%m/%d %H:%M:%S"),tmp1)
