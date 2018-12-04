#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:56:15 2018

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

#n = int(X*Y*0.5*0.0024375) #0.75 dia dot. Sharpie closer to 1 dia.

# If/Else statement for point # generation, unused for now.


a = raw_input("Would you like to apply dots [1] or lines [2]? ")
b = a.lower()
#Determines if a dot pattern or line pattern is applied.
f = open(raw_input("Enter Filename: ") +'.txt','w')
# Creates a text file for GCode to be added to. Allows user to name file.
f.write('G90' + '\n' + 'G21' + '\n' + 'G92 X0 Y0 Z0' 
        + '\n' + 'G0 X0 Y0 Z0' + '\n')
# Assigns GCode commands to initialize machine. Establishes absolute coords,
#metric units, sets home, and goes home.

if b in ["dots", "dot", "1"]:
    for i in range(0,201):
        x = random.randrange(0,X+1,2)
        y = random.randrange(0,Y+1,2)
        x_list.append(x)
        y_list.append(y)
        f.write('\n' + "G01 Z10")
        f.write('\n' + "G00 X"+str(x)+" Y"+str(y))
        f.write('\n' + "G01 Z-5")
elif b in ["lines", "line", "2"]:
    for i in range(0,201):
        x = random.randrange(0,X+1,2)
        y = random.randrange(0,Y+1,2)
        x_list.append(x)
        y_list.append(y)
        f.write('\n' + "G01 X"+str(x)+" Y"+str(y) + "f50")
else:
    print "Invalid Response. Try Again."
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
while j <= 201-1:
    t_list.append(calculateDistance(x_list[j],y_list[j],x_list[j+1],y_list[j+1]))
    j += 1
# Calculates the distance between each point generated, and adds to list.
t = 0
k = 0
while k <= 201-2:
    t += t_list[k] + t_list[k+1]
    k += 1

if b in ["dots", "dot", "1"]:
    print (t/50)/60 + (j*(30/2))/60
elif b in ["lines", "line", "2"]:
    print (t/50)/60
else:
    print "Error"
# Add all the distances together, divides them by the feed rate, and converts 
#time to minutes.
    
    
    #Patches that overlap, divid into subsets and have edges/corners overlap.