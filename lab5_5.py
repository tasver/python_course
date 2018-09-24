#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import math
print("Enter number: ")
n = int(input())

if n < 2:
    print("A number must be 2 and more")
elif n == 2:
    print("It is simple number")
i = 2
limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("It is not simple number")
        quit()
    i += 1
print("It is simple number")


