#!/usr/bin/env python3


#this script uses the sys module to take stdin output  and return it capatalized ie cat haiku.txt | capitalize.py 

import sys

for line in sys.stdin:
	print(line.strip().capitalize())


