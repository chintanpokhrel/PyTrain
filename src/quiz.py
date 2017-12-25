from sys import argv

class Question:
	def __init__(self, question, answer):
		self._question = question
		self._answer = answer

	@property
	def question(self):
		return self._question 

	@question.setter
	def set_question(self, question):
		self._question = question

	@property
	def answer(self):
		return self._answer

	@answer.setter
	def set_answer(self, answer):
		self._answer = answer

class Quiz:
	DELIM='######'
	def __init__(self, filename, path):
		
		import os
		os.chdir(path)

		self.questions = []
		
		for line in open(filename):
			line_arr = line.split(self.DELIM)
			self.questions.append(Question(line_arr[0], line_arr[1]))

		if len(self.questions) == 0:
			#TODO: Check if this is the right exception to raise
			raise ValueError('Nothing in the file')
	
	
	def get_question(self):
		import random
		que_num = int(random.random()*(len(self.questions)-1))
		return self.questions[que_num]

DATAFILE='data/questions.xml'
def addques():
	while True:
		q = raw_input("Question> ")
		a = raw_input("Answer> ")
	
		import xml_wrapper
		xml_wrapper.additem(q, a, DATAFILE)
		
		if checkquit():
			break



def master():
	print "What to do ?"
	print "1. Play"
	print "2. Add Question"
	choice = raw_input('Choice> ');
	if choice == '2':
		addques()
	
			
def checkquit():
	print "Enter a character to continue, q to quit"
	from getch import getch
	c = getch()
	if c == 'q' or c == 'Q':
		return True
	return False

def getrandom(n):
	from random import random
	from math import ceil
	return int(ceil(n*random()))

def play():
	n = raw_input('How many participants? ')
	print "Okay, let's play!"
	
	from xml_wrapper import getitem_at, numquestions
	nquest = numquestions()
	
	while True:
		participant = getrandom(n)
		print "Question goes for participant %s"%participant
	
		question, answer = getitem_at(getrandom(nquest), DATAFILE)
		print question
		
		if checkquit():
			break
		print answer 			

def _play():
	datafile_path = 'data'
	q = Quiz('quizzes.data', datafile_path)
		
	print "Let's have a pop quiz, here you go"
	while True:
		question = q.get_question()
		print question.question
		print "Press q to exit, anything else to continue"
		from getch import getch
		c = getch()
		if c == 'q' or c == 'Q':
			break
		print question.answer
		
	
	
