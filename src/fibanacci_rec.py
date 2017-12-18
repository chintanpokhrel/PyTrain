class BadFibanacci:
	def __init__(self):
		self.f = []
	
	def get(self, n):
		if n<=1:
			return 1
		return self.get(n-1) + self.get(n-2)
	

from sys import argv

try:
	num = int(argv[1])
	f = BadFibanacci()
	print f.get(num)
except ValueError:
	print "I can't print fibonacci for non ints idiot."
except IndexError:
	print "Here's how you use this program: %s num" % argv[0]
except Exception as e:
	print "Something unexpected, here's what happened:"
	print e

