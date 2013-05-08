"""
temperature.py
=====
Write a program that calculates celsius to fahrenheit based on user input.
1. Create a file called temperature.py
2. The program should ask for the temperature
3. Find the formula for this conversion here: http://math.about.com/od/formulas/a/temp.htm  
4. Implement it in your program
5. The program should output: c degrees celsius is f degrees fahrenheit
6. (obvs with f and c substituted with the appropriate calculated values)
7. Note that the outputs are floats!
8. You don't have to account for non-numeric input (at least... not yet!)

Example Output - Everything after the greater than sign (>) is user input:

Please enter a temperature in celsius
> 37
37.0 degrees celsius is 98.6 degrees fahrenheit
"""

import re

def c2f(celsius):
	if bool(re.search("[a-zA-Z `~!@#$%^&*()]", celsius)) != True:
		fahrenheit = (float(celsius)*9.0)/5 + 32
		return str(celsius) + " degrees celsius is " + str(fahrenheit) + " degrees fahrenheit"



usrinput = raw_input("Please enter a temperature in celsius\n> ")

while bool(re.search("[a-zA-Z `~!@#$%^&*()]", usrinput)) != True:
	print(c2f(usrinput))
	usrinput = raw_input("Please enter a temperature in celsius\n> ")

print("Goodbye!")