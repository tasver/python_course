#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import math
print("Enter your numbers: ")
x = float(input())
y = float(input())
z = float(input())

f = 1/(z*math.sqrt(2*math.pi))*math.exp(-((x-y)**2)/2*z**2)

print(f"x = {f}") 	
