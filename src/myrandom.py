class MyRandom:
	def __init__(self, limit):
		self.limit = limit

	def get(self):
		import random
		from math import ceil
		result = ceil(random.random()*self.limit)
		return result


