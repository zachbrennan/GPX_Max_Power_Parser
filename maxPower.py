import xml.etree.ElementTree as ET

tree = ET.parse('testFile.gpx')
powerTag = "{http://www.topografix.com/GPX/1/1}power"
root = tree.getroot()
steps = list(root.iter(powerTag))    

def maxIntPow(steps, interval):
    maxInt = 0
    
    for i in range(0,len(steps) - (interval - 1)):
        tempInt = 0
        for j in range(0, interval):
            tempInt += int(steps[i+j].text)
        tempInt /= interval
        
        if (tempInt > maxInt):
            maxInt = tempInt

    return maxInt


for i in range(1,len(steps)):
    print(str(i) + "s max:" , maxIntPow(steps, i))


