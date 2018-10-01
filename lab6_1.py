#! /usr/bin/python3
# -*- coding: utf-8 -*-
import math

def input_par() -> list:
	""" This function make input of data"""
	a, b, c = map(float, input('Enter 3 numbers: ').split())
	return [a, b, c]

def check_triangle(a:list) -> bool:
	""" This function check exists triangle"""
	if (((a[0] + a[1]) > a[2]) and ((a[0] + a[2]) > a[1]) and ((a[2] + a[1] > a[0]))):
		return True
	else:
		return False

def calculate(a:list) -> float:
	""" This function calculate area triangle """
	if check_triangle(a):
		half_perimetr = (a[0]+a[1]+a[2])/2
		area = math.sqrt(half_perimetr*(half_perimetr-a[0])*(half_perimetr-a[1])*(half_perimetr-a[2]))
		return area
	else: return 'Triangle not exists'
	
print(calculate(input_par()))
