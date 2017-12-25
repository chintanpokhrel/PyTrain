import xml_wrapper

def test_additem():
	question = 'What is your name'
	answer = 'no idea'
	datafile='test_questions.xml'
	xml_wrapper.additem(question, answer, datafile)
	
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file,datafile)
	root = tree.getroot()

	q = root.findall("./item/question")[0].text
	a = root.findall("./item/answer")[0].text

	assert q == question
	assert a == answer

	print "additem pass"
	import os
	os.remove(datafile)

test_additem()		

def test_getitem_at():
	question = 'What is your name'
	answer = 'no idea'
	datafile = 'test_questions.xml'
	xml_wrapper.additem(question, answer, datafile)

	q, a = xml_wrapper.getitem_at(1, datafile)
	
	assert q == question
	assert a == answer
	
	print "getitem_at pass"
	import os
	os.remove(datafile)

test_getitem_at()

