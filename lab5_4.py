#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import cmath
a, b, c = map(float, input('Enter 3 numbers: ').split())
discr = b**2-4*a*c

try:
    discr_squere=math.sqrt(discr)
except:
    discr_squere=cmath.sqrt(discr)

try:
    if discr < 0:
        x1=complex((-b+discr_squere)/(2*a))
        x2=complex((-b-discr_squere)/(2*a))
    elif discr == 0:
        x1 = -b / (2*a)
        x2 = -b / (2*a)
    elif discr > 0:
        x1 = (-b - discr_squere) / (2*a)
        x2 = (-b + discr_squere) / (2*a)
    print(f'X1={x1}\n X2={x2}')
except ZeroDivisionError:
    print('Error you can`t division on 0')
