def test_getch():
	
	from getch import getch
	print "Enter the lowercase character a: "
	c = getch()
	assert c == 'a'
	print "getch pass"
	
test_getch()
