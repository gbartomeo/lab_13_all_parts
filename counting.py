"""
counting.py
======

Print out  "I'm on <count number>".  Count by ones from exactly -3 up to and including 3.  If the absolute value of the count is equal to 1, add three question marks.  Do this twice: once with a while loop, and again with a for loop. 

Example Output:

I'm on -3
I'm on -2
I'm on -1???
I'm on -0
I'm on 1???
I'm on 2
I'm on 3

a) Do this once using a while loop.

b) Do this again using a for loop.
"""

print(" WHILE LOOP\n------------")
i = -3
while i<4:
	if (i < 0 and i * -1 == 1) or (i > 0 and i*1 == 1):
		print("I'm on " + str(i) + "?"*3)
	else:
		print("I'm on " + str(i))
	i+=1

print("\n\n FOR LOOP\n----------")
for i in range(-3,4):
	if (i < 0 and i * -1 == 1) or (i > 0 and i*1 == 1):
		print("I'm on " + str(i) + "?"*3)
	else:
		print("I'm on " + str(i))