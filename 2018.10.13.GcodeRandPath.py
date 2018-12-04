#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:41:13 2018

@author: kyyiv
"""

import random
# Allows for random generation of numbers.
import matplotlib.pyplot as plt
# Allows for plot of machine path.
import math
# Allows for square roots to be taken.
def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist
# Function that gives the distance between two points.

X = float(raw_input("What is the X length? "))
Y = float(raw_input("What is the Y length? "))
# Has user input X and Y lengths of the specimen.
x_list = [0]
y_list = [0]
# Generates an empty list for each axis for future plot.
if X >= Y:
    n = X
    
else:
    n = Y
# If/Else statement for point # generation, unused for now.
f = open(raw_input("Enter Filename: ") +'.txt','w')
# Creates a text file for GCode to be added to. Allows user to name file.
f.write('G90' + '\n' + 'G21' + '\n' + 'G92 X0 Y0 Z0' 
        + '\n' + 'G0 X0 Y0 Z0' + '\n')
# Assigns GCode commands to initialize machine. Establishes absolute coords,
#metric units, sets home, and goes home.
for i in range(0,101):
    x = random.randrange(0,X+1,2)
    y = random.randrange(0,Y+1,2)
    x_list.append(x)
    y_list.append(y)
    f.write('\n' + "G01 X"+str(x)+" Y"+str(y))
# Generates X and Y values randomly, adds them to axis lists, and prints
#points to text file for movement.
f.write('\n')
f.write('\n' + 'M00')
# End command.
f.close()
# Closes text file. Important because without this command file is unusable.
plt.plot(x_list, y_list)
# Plots points and creates a path between them, giving visual representation.
t_list = []
# Empty list for storing distance values between points.
j = 0
while j <= 100:
    t_list.append(calculateDistance(x_list[j],y_list[j],x_list[j+1],y_list[j+1]))
    j += 1
# Calculates the distance between each point generated, and adds to list.
t = 0
k = 0
while k <= 99:
    t += t_list[k] + t_list[k+1]
    k += 1
print (t/50)/60
# Add all the distances together, divides them by the feed rate, and converts 
#time to minutes.