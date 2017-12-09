class FibanacciGen:
	def __init__(self, n):
		self.a = -1
		self.b = 1
		self.c = self.a + self.b
		self.n = n


	def get(self):
		while self.c < self.n:	
			self.a = self.b
			self.b = self.c
			self.c = self.a + self.b
			yield self.c

#print list(FibanacciGen(10).get())



f = FibanacciGen(10).get()


print f.next()

print f.next()

print f.next()

print f.next()

print f.next()

print f.next()

print f.next()

print f.next()


#for f in FibanacciGen(20).get():
#	print f	
