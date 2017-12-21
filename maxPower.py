import xml.etree.ElementTree as ET
import plotly
from plotly.graph_objs import Scatter, Layout
import time
import sys

t = time.time()

interval = 120
if (len(sys.argv) > 1):
    interval = int(sys.argv[1])

tree = ET.parse('testFile.gpx')
powerTag = "{http://www.topografix.com/GPX/1/1}power"
root = tree.getroot()
steps = list(root.iter(powerTag))    

#def maxIntPow(steps, interval):
#    maxInt = 0
#    
#    for i in range(0,len(steps) - (interval - 1)):
#        tempInt = 0
#        for j in range(0, interval):
#            tempInt += int(steps[i+j].text)
#        tempInt /= interval
#       
#        if (tempInt > maxInt):
#            maxInt = tempInt
#
#    return maxInt

def maxIntPow(steps, interval):
    maxInt = 0
    tempInt = 0

    for k in range(0, interval):
        tempInt += int(steps[k].text)

    for i in range(interval,len(steps) - (interval - 1)):

        tempInt -= int(steps[i-interval].text)
        tempInt += int(steps[i].text)

        if (tempInt > maxInt):
            maxInt = tempInt
    
    #print( str(interval) + "s power:" + str(maxInt / interval))

    return maxInt / interval

data = list()
#for i in range(1,len(steps)):
for i in range(1,interval + 2): 
    t2 = time.time()
    maxInt = maxIntPow(steps, i)
    data.append(maxInt)
    #print("Loop time:", time.time() - t2)

plotly.offline.plot({
    "data": [Scatter(x=range(1,len(data)), y=data)],
    "layout": Layout(title="Power Curve")
})

elapsed = time.time() - t
print("Elapsed time:" + str(elapsed))
