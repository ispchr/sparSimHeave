"""
    Author: 
    Description: Extracts heave movements from the floating body
    How to use: Simple script for now
    Date: Jan - 2021
    Version: 2.0
"""

import matplotlib.pyplot as plt
import re


# --------------------- RETRIEVING ROLL AND TIME FROM LOG FILES --------------------------------------
def extractor(endTime, timeStep):
    # Heave array
    z_CFD = []
    # Time array
    time_CFD = []
    for i in range(int(endTime / timeStep)):
        # Ignoring initial heave
        if i == 0:
            continue
        else:
            # Calculating time instant 
            t = timeStep * i
            t = round(t, 1)
            # Removes trailing zeros
            t = f'{t:g}'
            time_CFD.append(float(t))
            # Extracting centerOfRotation tensor from the 6DoF's outputs
            raw = open(fr"processor0/{time}/uniform/sixDoFRigidBodyMotionState", "r")
            for line in raw:
                centreOfRotation = "centreOfRotation"
                # Getting the line where string "centreOfRotation" is found
                if centreOfRotation in line:
                    # Extracting floats only (ignoring strings)
                    vector = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", line)
                    # Getting heave values only
                    z = float(vector[2])
                    z_CFD.append(z)
    return z_CFD, time_CFD


# Retrieving values from log files
endTime = 20
timeStep = 0.1
heave, time = extractor(endTime, timeStep)
# --------------------- PLOTTING --------------------------------------
# Plotting CFD retrieved values
plt.figure(2)
plt.plot(time, heave, label="Heave", linewidth=1)
plt.xlabel('Time(s)')
plt.ylabel('Heave(m)')
plt.grid()
plt.legend()
plt.show()
