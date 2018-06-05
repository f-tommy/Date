#!/usr/bin/env python3
# echo "yyyy/mm/dd hh:mm:ss" | datechange.py arg
# Transform time zone
# arg: hours for timechange
import fileinput
import argparse
from datetime import datetime
from datetime import timedelta

# Obtain argument
parser = argparse.ArgumentParser()
parser.add_argument("td",type=int)
parser.add_argument("files",metavar='FILE', nargs='*')
args = parser.parse_args()

# Process line input
for line in fileinput.input(files=args.files):
    lin = line.rstrip('\n')
    col = lin.split()
    date1 = datetime.strptime(' '.join(col[0:2]),"%Y/%m/%d %H:%M:%S")
    date2 = date1 + timedelta(hours=args.td)
    tmp1 = ' '.join(col[2:]) # list to string
    print(date2.strftime("%Y/%m/%d %H:%M:%S"),tmp1)
