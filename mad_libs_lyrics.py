"""
mad_libs_lyrics.py
====
* using your lyrics from lyrics.py, replace 4 words with variables
* set your variables equal to strings at the top of the file
* name the variables after the part of speech of the word they are replacing,
  followed by a number:

  adjective1 = 'tiny'
  adjective2 = 'magical'
  noun1 = 'ukulele'

* print the new lyrics with variables to the console
"""

plnoun1 = "harvests"
noun1 = "heart"
verb1 = "reap"
verb2 = "silencing"

line = [1,2,3,4,5]
line[0] = "There were " + plnoun1 + " when each hour was a war I fought to survive"
line[1] = "There were " + plnoun1 + " full of nightmares and I dreaded " + verb2 + " my " + noun1
line[2] = "There were skies that burst open with a downpour to " + verb1 + " me alive"
line[3] = "But the world took a spark like a match in the dark"
line[4] = "And the fire brought me to life"

for each in line:
	print(each)