"Log Muncher"
import csv
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
script, param, log = argv


log = open(log, "r")
csvlog = csv.reader(log)

x = []
y = []

for row in csvlog:
	if param in row: 
		print row
		x.append(float(row[3]))
		y.append(float(row[4]))

plt.plot(x)
plt.plot(y)
plt.grid(True)
plt.suptitle(param)  
plt.show()

"""
searchlines = log.readlines()
for i, line in enumerate(searchlines):
    if param in line: print line
"""

ATT = ['TimeUS','DesRoll','Roll','DesPitch','Pitch','DesYaw','Yaw','ErrRP','ErrYaw']
howmany = len(param)