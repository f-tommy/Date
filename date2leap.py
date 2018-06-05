#!/usr/bin/env python3
# echo "yyyy/mm/dd" | date2leap.py
# Calculate leap seconds (gps - UTC)
import fileinput
import math
from datetime import datetime
from datetime import timedelta

def dcal(x):
    ctmp = str(x).split('/')
    year = str(ctmp[0])
    ref = datetime.strptime(str(ctmp[0]),"%Y") # Year
    date = datetime.strptime(x,"%Y/%m/%d")
    td = date - ref
    cal = int(year) + ( td.days + 1 ) / 365.25
    return cal

t = [0] * 20
t[0] = dcal('1980/01/01')
t[1] = dcal('1981/07/01')
t[2] = dcal('1982/07/01')
t[3] = dcal('1983/07/01')
t[4] = dcal('1985/07/01')
t[5] = dcal('1988/01/01')
t[6] = dcal('1990/01/01')
t[7] = dcal('1991/01/01')
t[8] = dcal('1992/07/01')
t[9] = dcal('1993/07/01')
t[10] = dcal('1994/07/01')
t[11] = dcal('1996/01/01')
t[12] = dcal('1997/01/01')
t[13] = dcal('1999/01/01')
t[14] = dcal('2006/01/01')
t[15] = dcal('2009/01/01')
t[16] = dcal('2012/07/01')
t[17] = dcal('2015/07/01')
t[18] = dcal('2017/01/01')
t[19] = dcal('2200/01/01')

for line in fileinput.input():
    lin = line.rstrip('\n')
    col = lin.split()
    cal0 = dcal(col[0])
    for n in range(19):
        nn = n + 1
        if (cal0 >= t[n]) and (cal0 < t[nn]):
            print(n)

