#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import math

print "Enter three sizes: "
a = int(input())
b = int(input())
c = int(input())

if (((a + b) > c) and ((a + c) > b) and ((c + b) > a)):
    print "Triangle exists"
else:
    print "Triangle does not exist"
