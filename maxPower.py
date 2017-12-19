import xml.etree.ElementTree as ET
tree = ET.parse('testFile.gpx')
root = tree.getroot()

print(root)

for powerStep in root.iter("{http://www.topografix.com/GPX/1/1}power"):
    print(powerStep.text)


