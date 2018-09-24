#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import math
print("Enter input data: ")
a, b, c = map(float, input().split())

discr = b**2 - 4*a*c;
#print(f 'Discriminant = {discr}')
if discr > 0:
	x1 = (-b + math.sqrt(discr)) / (2*a)
	x2 = (-b - math.sqrt(discr)) / (2*a)
#	print(f ' x1 = {x1} x2 = {x2}')
elif discr == 0:
	x = -b/(2*a)
	print (f 'x = {x}')

#formula = a*x**2+b*x+c=0
#print (a,b,c)
