import xml.etree.ElementTree as ET
import plotly
from plotly.graph_objs import Scatter, Layout

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


data = list()
#for i in range(1,len(steps)):
for i in range(1,61): 
    maxInt = maxIntPow(steps, i)
    data.append(maxInt)

plotly.offline.plot({
    "data": [Scatter(x=range(1,61), y=data)],
    "layout": Layout(title="Power Curve")
})
