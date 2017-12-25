'''This is called a docstring. When you do:
import number_game

and do

help(number_game)

this string is printed. Try it'''

class Game:
	'''Explain what this class is for here'''

	def __init__(self, _max_chances=5):
		'''This is the constructor, initialize self.max_chances to user provided value'''
		#Your code here. HINT below:
		#self.max_chances = 
		pass #pass means do nothing

	def getrandom(self):
		#This is how you import from other files
		#calling random() will give you a random real no b/w 0 and 1
		#Convert it into a number b/w 1 and 100 and return it
		from random import random
		#Your code here
		pass

	def getinput(self):
		#The raw_input() function can be used to get user input.
		#It gives you a string, use int() to convert it into an integer
		#Get input, convert into an int and return the value
		#Your code here
		pass

	def play(self):
		'''Explain how this works here'''
		#1. Call self.getrandom() that you've written above to get a random number
		random_number = self.getrandom()
		#2. Define a loop variable and loop until max chances, you can use a while loop here
		#Your code here
			#2.1 Ask the user for input using self.getinput()
			#Your code here

			#2.1 Compare it with random_number
			#    If what the user entered was smaller than random_number, print "Too small, try something bigger"
			#    If it was bigger, print "Too big, try smaller
			#    If equal, the user wins. print "You win!! :D" and break
			#Your code here

			#2.3 Increment your loop variable
		#3. Outside the loop, check if loop variable == max_chances
		#   If yes, print "Your chances are over. You lose!!"
		#Your code here
	
from utils import checkquit		

def play():
	#This is how you create an object
	g = Game(10)
	while True:
		if checkquit(): #This is defined in utils.py, asks a user if they want to continue or quit
			break
`
		g.play()
