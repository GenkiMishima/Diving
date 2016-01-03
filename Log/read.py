import xml.etree.ElementTree as ET
tree = ET.parse('log.xml')
root = tree.getroot()
elelist= root.findall(".//Date")
Place = []
Date = []
for ele in elelist:
	if not ele in Date:
		Date.append(ele.text)
	#print (ele.text);
print Date
	
