#! /usr/bin/python3
# -*- coding: utf-8 -*-
import math

def input_par() -> float:
	""" This function make input of summ deposit, expected_amount, percents"""
	summ, expected_amount, percent =  map(float, input('Enter your summ deposit, expected_amount, percents: ').split())
	return [summ, expected_amount, percent]

def calculate(a:list) -> float:
	""" This function calculate end of deposit year """
	summ, expected_amount, percent = a
	year = 0
	while summ <= expected_amount:
		summ = summ + (summ*(percent/100))
		year = year+1
	return year
	
print(calculate(input_par()))
