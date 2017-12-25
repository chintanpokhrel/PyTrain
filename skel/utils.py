def checkquit():
	from time import sleep
	sleep(5)
	print "\nEnter a character to continue, q to quit"
	from getch import getch
	c = getch()
	if c == 'q' or c == 'Q':
		return True
	return False

def getrandom(n):
	from random import random
	from math import ceil
	return int(ceil(n*random()))


def getinput(show=''):
	#https://stackoverflow.com/a/11664675
	sentinel = ''
	return '\n'.join(iter(lambda: raw_input(show), sentinel))

