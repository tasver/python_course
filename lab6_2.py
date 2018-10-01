#! /usr/bin/python3
# -*- coding: utf-8 -*-
import math

def input_par() -> list:
	""" This function make input of summ deposit, percent, years """
	summ, percent, years =  map(float, input('Enter your summ deposit, percent, years: ').split())
	return [summ, percent, years]

def calculate(a:list) -> float:
	""" This function calculate end of deposit """
	summ, percent, years = a
	i = 1
	while i <= years:
		i = i+1;
		percents_year = summ*(percent/100)
		summ = summ + percents_year
	return summ
	
print(calculate(input_par()))
