#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
print("Enter height and width door: ")
height, width = input().split()
print('Enter a, b, c dimensions of the box: ')
a, b, c =  input().split()
#print(height, width, a, b,c)
count = int(0)
if (int(a) <= (int(height) or int(width))):
	count = count + 1
if (int(b) <= (int(height) or int(width))):
	count = count + 1
if (int(c) <= (int(height) or int(width))):
	count = count + 1	
if (count >= 2):
	print(count)
	print ("succes")
else: 
	print("false")

	print(count)
