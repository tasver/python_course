
#! /usr/bin/python3
# -*- coding: utf-8 -*-
from decimal import Decimal
def input_number() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your string: '))
	return input_string

def sorted_words(string:str) -> str:
	""" This function sorted words word"""
	return ' '.join(sorted(string.split(), key=len))
	        

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(sorted_words(input_number()))
