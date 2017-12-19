import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('testFile.gpx').getroot()

print(e)
