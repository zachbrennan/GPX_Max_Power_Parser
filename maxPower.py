import xml.etree.ElementTree as ET
import plotly
from plotly.graph_objs import Scatter, Layout
import time
import sys


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

