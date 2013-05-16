""" 
fortune.py
=====
Write a program that generates a random fortune.

You'll be using the random module.

1. Ask the user if they want to see the future.
2. If the answer yes, y, or yeah, then use the rand int function to generate a random number between 1 and 5.
3. Create 5 fortunes.
4. Based on the number that is generated, output one of the fortunes that you created.
5. If the answer isn't yes, say "I didn't want to tell you anyway"

Example Output (consider text after the ">" user input):

Run 1:
-----
Would you like to see your fuuuuttttuuuurrreee? > yes
You'll have a pastry today.

Run 2:
-----
Would you like to see your fuuuuttttuuuurrreee? > yes
There are many quotation marks in your future!

Run 3:
-----
Would you like to see your fuuuuttttuuuurrreee? > no
I didn't want to tell you anyway
"""

import random
fortunes = ["You will eat something today", "There is a bug living in your home", "There will be a problem with the subway", "You will sleep tonight", "You will wear pajamas tonight"]
if raw_input("Would you like to see your fuuuuttttuuuurrreee? > ") in ["Yes", "yes", "y", "yeah", "YEAH", "YES"]:
	print(fortunes[random.randint(0,4)])
else:
	print("I didn't want to tell you anyway")