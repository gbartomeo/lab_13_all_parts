"""
lyrics.py
=====
* write three programs that all do the same thing!
* all of these programs should:
  * print out the same four lines from your favorite song
  * each line of lyrics should be printed out on a new line
  * for example, if your program prints out the song, 'On a Tropical Island', 
    the output would look like (of course, with three version, imagine this
    three times): 

On a tropical island,
Underneath a molten lava moon.
Hangin' with the hula dancers,
Askin' questions cause' they got all the answers.

* there are multiple ways of printing out strings on new lines:
  * maybe it's just one command
  * or several commands
  * or use different ways of representing strings, putting strings 
    together, or incorporating newlines
* write THREE DIFFERENT versions of this program in this file 
"""

line1 = "There were days when each hour was a war I fought to survive"
line2 = "There were nights full of nightmares and I dreaded closing my eyes"
line3 = "There were skies that burst open with a downpour to drown me alive"
line4 = "But the world took a spark like a match in the dark"
line5 = "And the fire brought me to life"

lines = [line1, line2, line3, line4, line5]

# Version 1

print("There were days when each hour was a war I fought to survive\nThere were nights full of nightmares and I dreaded closing my eyes\nThere were skies that burst open with a downpour to drown me alive\nBut the world took a spark like a match in the dark\nAnd the fire brought me to life")

# Version 2

print(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5)

# Version 3

for each in lines:
	print(each)