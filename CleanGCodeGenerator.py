#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:49:20 2018

@author: kyyiv
"""

import random
# Allows for random generation of numbers.

X = float(input("What is the X length? "))
Y = float(input("What is the Y length? "))
# Has user input X and Y lengths of the specimen.

x_list = [0]
y_list = [0]
# Generates an empty list for each axis for future plot.

#n = int(X*Y*0.5*0.0024375) #0.75 dia dot. Sharpie closer to 1 dia.

L = 50 # Number of lines - affects density of patch.

P = 20 # Pen adjustment - affects the overlap created by the pens and increases the likelihood of filling gaps.

I = 0.2*X
J = 0.2*Y
# Generates subset lengths based on original/given lengths.

a = input("Would you like to apply dots [1] or lines [2]? ")
b = a.lower()
# Determines if a dot pattern or line pattern is applied.

f = open(input("Enter Filename: ") +'.txt','w')
# Creates a text file for GCode to be added to. Allows user to name file.

f.write('G90' + '\n' + 'G21' + '\n' + 'G92 X0 Y0 Z0' 
        + '\n' + 'G0 X0 Y0 Z0' + '\n' + 'G1 Z-10' + '\n')
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
# Creates GCode for applying a dot pattern.
elif b in ["lines", "line", "2"]:
    F = 0
    R = 0
# Initiallizes subset tracking.
    for F in range(0,6):
        f.write('\n' + "G01 Y"+str(0.8*J*F) + " f50" + '\n')
# Controls movement along y-axis for subsets.
        for R in range(0,6):
            if F in [0, 2, 4]:
                for i in range(0,L+1):
                    x = random.randrange(int((0.8*I*R)+P),int(I*(1+(0.8*R)))+P+1,2)
                    y = random.randrange(int((0.8*J*F)+P),int(J*(1+(0.8*F)))+P+1,2)
                    x_list.append(x)
                    y_list.append(y)
                    f.write('\n' + "G01 X"+str(x)+" Y"+str(y) + " f50")
                f.write('\n')
                f.write('\n' + "G01 X"+str(I*R)+" Y"+str(J*F) + " f50" + '\n')
# Generates random line endpoints within a subset and moves subsets left to right.
            elif F in [1, 3, 5]:
                for i in range(0,L+1):
                    x = random.randrange(int((0.8*I*R)+P),int(I*(1+(0.8*R)))+P+1,2)
                    y = random.randrange(int((0.8*J*F)+P),int(J*(1+(0.8*F)))+P+1,2)
                    x_list.append(x)
                    y_list.append(y)
                    f.write('\n' + "G01 X"+str(x)+" Y"+str(y) + " f50")
                f.write('\n')
                f.write('\n' + "G01 X"+str(I*(6-R))+" Y"+str(J*F) + " f50" + '\n')
# Generates random line endpoints within a subset and moves subsets right to left.

else:
    print ("Invalid Response. Try Again.")
# Generates X and Y values randomly, adds them to axis lists, and prints
#points to text file for movement.
f.write('\n' + 'G1 X0 Y0 Z0' + '\n')
f.write('\n' + 'M00')
# End command.
f.close()
# Closes text file. Important because without this command the file is unusable.