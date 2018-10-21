
#! /usr/bin/python3
# -*- coding: utf-8 -*-
from decimal import Decimal
def input_number() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your number: '))
	return input_string

def check_number_lucky(number:str) -> str:
	""" This function make fizz or buzz string"""
	result_string = str()

	if ((len(number))%2 == 0):
	    number_first = number[0:int(len(number)/2)]
	    number_second = number[int(len(number)/2):]
	    sum_first = sum(Decimal(i) for i in number_first)
	    sum_second = sum(Decimal(i) for i in number_second)
	    if sum_first == sum_second:
	        return "TRUE"
	    else: 
	        return "FALSE"
	else:
	    number_first = number[0:int(len(number)/2)]
	    number_second = number[int(len(number)/2)+1:]
	    sum_first = sum(Decimal(i) for i in number_first)
	    sum_second = sum(Decimal(i) for i in number_second)
	    if sum_first == sum_second:
	        return "TRUE"
	    else: 
	        return "FALSE"
	        

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(check_number_lucky(input_number()))
