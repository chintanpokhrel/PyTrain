from sys import argv
from utils import *

DATAFILE='data/questions.xml'

def start():
	print "What to do ?"
	print "1. Play"
	print "2. Add Question"
	choice = raw_input('Choice> ');
	
	if choice == '1':
		play()
	elif choice == '2':
		addques()
	
			
def play():
	n = int(raw_input('How many participants? '))
	print "Okay, let's play!"
	
	from xml_wrapper import getitem_at, numquestions
	nquest = numquestions(DATAFILE)

	while True:
		participant = getrandom(n)

		print "-----------------------------------------------------"
		print "\nQuestion goes for participant %s"%participant

		print getrandom(nquest)
		print nquest
	
		question, answer = getitem_at(getrandom(nquest), DATAFILE)
		print "Question: " + question
		
		if checkquit():
			break
		print '\nAnswer: ' + answer 			
	
		if checkquit():
			break


def addques():
	while True:
		q = getinput("Question> ")
		a = getinput("Answer> ")
	
		import xml_wrapper
		xml_wrapper.additem(q, a, DATAFILE)
		
		if checkquit():
			break

