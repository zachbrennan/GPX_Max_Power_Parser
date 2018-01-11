from maxPower import maxIntPow
import xml.etree.ElementTree as ET
import plotly
from plotly.graph_objs import Scatter, Layout
import time
import sys

t = time.time()

interval = 120

if (len(sys.argv) < 2):
    exit("No file arg")
else:
    fileName = sys.argv[1]
if (len(sys.argv) > 2):
    if (int(sys.argv[2] > 0)):
        interval = int(sys.argv[2])
    

tree = ET.parse(fileName)
powerTag = "{http://www.topografix.com/GPX/1/1}power"
root = tree.getroot()
steps = list(root.iter(powerTag))    

data = list()

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

