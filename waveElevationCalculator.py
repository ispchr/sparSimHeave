"""
    Author: 
    Description: Extracts wave elevations through alpha.water's run-time line sample
    How to use: Simple script for now
    Date: Jan - 2021
    Version: 2.0
"""

import numpy as np
import matplotlib.pyplot as plt


def extractor(timeStamp):
    # Opening the line sample
    raw = np.genfromtxt(fr"postProcessing/line/{timeStamp}/afterObject_alpha.water.xy", delimiter=" ")
    # looking for z-coordinate that has alpha value closer to 0.5
    raw = np.column_stack((raw, np.abs(0.5 - raw[:, 1])))
    freeSurfaceElevation = raw[np.argmin(raw[:, 2]), 0]
    return freeSurfaceElevation


freeSurfaceElevations = []
time = []
# Defining still water level, time step and final time 
SWL = 1.5
timeStep = 0.1
endTime = 20
for i in range(int(endTime / timeStep)):
    if i == 0:
        continue
    else:
        timeInstant = timeStep * i
        # Rounds float to 2 decimal places
        timeInstant = round(timeInstant, 1)
        # Removes trailing zeros
        timeInstant = f'{timeInstant:g}'
        # Appending time list
        time.append(timeInstant)
        # Appending for surface elevations using extractor function
        freeSurfaceElevations.append(extractor(timeInstant) - SWL)

plt.scatter(time, freeSurfaceElevations)
plt.show()
