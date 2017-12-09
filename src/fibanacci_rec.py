class BadFibanacci:
	def __init__(self):
		self.f = []
	
	def get(self, n):
		if n==1 or n==0:
			return 1
		return self.get(n-1) + self.get(n-2)
	

f = BadFibanacci()

print f.get(150)
