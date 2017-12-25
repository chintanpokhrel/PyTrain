class Parser:
	def __init__(self, everything=''):
		self.everything=everything

	def parse(self):
		'''Given a string with tags <question></question>, <answer></answer>, return a question answer dictionary'''
		
