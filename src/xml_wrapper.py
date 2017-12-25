import xml.etree.ElementTree as ET


def additem(_question, _answer, datafile):
	try:
		tree = ET.parse(datafile)
		root = tree.getroot()
	except IOError:
		root = ET.Element('data')
		tree = ET.ElementTree(element=root)
			
	item = ET.SubElement(root, 'item')
	question = ET.SubElement(item, 'question')
	answer = ET.SubElement(item, 'answer')
	question.text = _question
	answer.text = _answer

	tree.write(datafile)

def getitem_at(pos, datafile):
	tree = ET.ElementTree(file=datafile)
	root = tree.getroot()
	pos = str(pos)
	return root.findall('./item['+pos+']/question')[0].text, root.findall('./item['+pos+']/answer')[0].text;


def numquestions(datafile):
	tree = ET.ElementTree(file=datafile)
	root = tree.getroot()
	
	return len(root.findall('./item'))	
