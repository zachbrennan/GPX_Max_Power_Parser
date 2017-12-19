import xml.etree.ElementTree as ET
tree = ET.parse('testFile.gpx')
root = tree.getroot()


totalSteps = 0
totalPower = 0
avgPower = 0
maxPower = 0

for powerStep in root.iter("{http://www.topografix.com/GPX/1/1}power"):
    totalPower += int(powerStep.text)
    totalSteps += 1
    if (int(powerStep.text) > maxPower):
        maxPower = int(powerStep.text)

avgPower = totalPower / totalSteps
print("Sum of power numbers:" , totalPower)
print("Average Power:" , avgPower)
print("Max 1s Power:" , maxPower)


