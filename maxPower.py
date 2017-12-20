import xml.etree.ElementTree as ET

tree = ET.parse('testFile.gpx')
root = tree.getroot()

def maxOneSecond(root):
    maxPower = 0

    for powerStep in root.iter("{http://www.topografix.com/GPX/1/1}power"):
        if (int(powerStep.text) > maxPower):
            maxPower = int(powerStep.text)

    print("Max 1s Power:" , maxPower)

def maxThreeSecond(root):
    
    maxThree = 0
    steps = list(root.iter("{http://www.topografix.com/GPX/1/1}power"))

    for i in range(0,len(steps) - 2):
        tempThree = ((int(steps[i].text) + int(steps[i+1].text) + int(steps[i+2].text)) / 3)
        if (tempThree > maxThree):
            maxThree = tempThree

    print("Max 3s Power:", maxThree)
    
def maxIntPow(root, interval):
    maxInt = 0
    steps = list(root.iter("{http://www.topografix.com/GPX/1/1}power"))
    
    for i in range(0,len(steps) - (interval - 1)):
        tempInt = 0
        for j in range(0, interval):
            tempInt += int(steps[i+j].text)
        tempInt /= interval
        
        if (tempInt > maxInt):
            maxInt = tempInt

    print("Max " + str(interval) + "s Power:" + str(maxInt))

maxOneSecond(root)
maxThreeSecond(root)
maxIntPow(root, 5)
