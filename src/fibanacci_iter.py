class Fibanacci:
	def __init__(self, n=1):
		self.a = -1
		self.b = 1
		self.c = self.a + self.b
		self.n = n

	def __iter__(self):
		return self

	def next(self):
		if self.c < self.n:
			self.a = self.b
			self.b = self.c
			self.c = self.a + self.b
			return self.c
		else:
			raise StopIteration()

print list(Fibanacci())

print list(Fibanacci(-1))

print list(Fibanacci(1000))

print list(Fibanacci(0))


#for f in fib:
#	print f

