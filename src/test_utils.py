from utils import *

def test_getinput(show=''):
	print "Enter the below on the prompt"
	print "B for Ball"
	print "A for apple"
	s = getinput(show)
	print "Verify that the o/p is what you entered:"
	print s
