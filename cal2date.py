#!/usr/bin/env python3
# echo "year cal" | cal2date.py
import fileinput
from datetime import datetime, date, timedelta
from datetime import timedelta

for line in fileinput.input():
 tmp0 = line.rstrip('\n')
 col = tmp0.split()
 ref = datetime.strptime(str(int(col[0])),"%Y") # Year
 cal = int(col[1]) - 1 # Cal
 tmp1 = ' '.join(col[2:]) # list to string
 date = ref + timedelta(days=cal)
 print(date.strftime("%Y/%m/%d"),tmp1)
