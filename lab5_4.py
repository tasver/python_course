#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

a, b, c = map(float, input('Enter 3 numbers: ').split())
if a == 0 and b != 0:
    x1 = x2 = -(c / b)
elif a == 0 and b == 0:
    x1 = x2 = Any
else:
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + discriminant ** 0.5)/2 * a
    x2 = (-b - discriminant ** 0.5)/2 * a
print(f'X1={x1}\n X2={x2}')
