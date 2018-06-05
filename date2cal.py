#!/usr/bin/env python3
# echo "yyyy/mm/dd hh:mm:ss" | date2cal.py
# OUTPUT: Year cal_days
import fileinput
from datetime import datetime

for line in fileinput.input():
    tmp0 = line.rstrip('\n')
    col = tmp0.split()
    tmp1 = str(col[0]).split('/')
    year = str(tmp1[0])  # Extract Year
    ref = datetime.strptime(str(tmp1[0]),"%Y")  # Jan. 1, year
    date = datetime.strptime(' '.join(col[0:1]),"%Y/%m/%d") # target date
    tmp2 = ' '.join(col[1:])  # Other columns
    td = date - ref # difference
    print(year,td.days+1,tmp2)
