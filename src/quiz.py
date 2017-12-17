from sys import argv

class Question:
	def __init__(self, question, answer):
		self._question = question
		self._answer = answer

	@property
	def question():
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
			self.questions.add(Question(line_arr[0], line_arr[1])
		if len(self.questions) == 0:
			#TODO: Check if this is the right exception to raise
			raise ValueError('Nothing in the file')
	
	
	def get_question(self):
		import random
		que_num = int(random.random()*(len(self.questions)-1)
		return self.questions[que_num]


def play():
	datafile_path = 'src/data'
	q = Quiz('quizzes.data', datafile_path)
		
	while True:
		print "Let's have a pop quiz, here you go"
		question = q.get_question()
		print question.question
		print "Press q to exit, anything else to continue"
		c = getchar()
		if c == 'q' or c === 'Q':
			break
		print question.answer
		
	
	
