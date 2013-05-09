"""
dice.py
=====
Roll two four-sided dice 1000 times.  Keep track of the number of each potential result (2 - 8). 

* create a histogram showing the results 
* you can count by 10's using an x to represent each 10 in the histogram... 
* you can use division, the built in round() function, and int to convert from float to int to get the number of x's to do this
* for example: round(2.5) returns a float... use int to change it to an int: int(round(2.5))... and finally use that to multiply your string

2 xxxxxx
3 xxxxxxxxxxx
4 xxxxxxxxxxxxxxxxxx
5 xxxxxxxxxxxxxxxxxxxxxxxx
6 xxxxxxxxxxxxxxxxxx
7 xxxxxxxxxxxxx
8 xxxxxxx
"""

import random

numspos = [2,3,4,5,6,7,8]
numsrolled = [0,0,0,0,0,0,0]

for each in range(1000):
	roll = random.randint(1,4) + random.randint(1,4)
	numsrolled[numspos.index(roll)] += 1

for each in numsrolled:
	print(str(numspos[numsrolled.index(each)]) + " " + "x"*(int(each/10)))