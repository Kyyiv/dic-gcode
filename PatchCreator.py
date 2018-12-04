#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:10:40 2018

@author: kyyiv
"""

F = 0
R = 0

for F in range(0,6):
    f.write('\n' + "G01 Y"+str(0.8*J*F) + "f50")
    
    for R in range(0,6):
        if F in [0, 2, 4]:
            for i in range(0,201):
                x = random.randrange(int((0.8*I*R)),int(I*(1+(0.8*R)))+1,2)
                y = random.randrange(int((0.8*J*F)),int(J*(1+(0.8*F)))+1,2)
                x_list.append(x)
                y_list.append(y)
                f.write('\n' + "G01 X"+str(x)+" Y"+str(y) + "f50")
                f.write('\n' + "G01 X"+str(0.8*I*R)+" Y"+str(0.8*J*F) + "f50")
        if F in [1, 3, 5]:
            for i in range(0,201):
                x = random.randrange(int((0.8*I*R)),int(I*(1+(0.8*R)))+1,2)
                y = random.randrange(int((0.8*J*F)),int(J*(1+(0.8*F)))+1,2)
                x_list.append(x)
                y_list.append(y)
                f.write('\n' + "G01 X"+str(x)+" Y"+str(y) + "f50")
                f.write('\n' + "G01 X"+str(0.8*I*(6-R))+" Y"+str(0.8*J*F) + "f50")
        F += 1
        R += 1