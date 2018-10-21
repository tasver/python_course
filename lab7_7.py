
#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_str() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your string: '))
	return input_string

def string_to_camel_case(string:str) -> str:
	""" This function make camel case string"""
	result_camel_case = str()
	sym = iter(string)
	for symb in sym:
	    if symb == "_":
	        symbol = next(sym)
	        symb = "" + symbol.upper()
	    result_camel_case += symb
	return result_camel_case
	
def string_to_snake_case(string:str) -> str:
    """ This function make case snake string"""
    result_snake_case = str()
    for symb in string:
        if symb.isupper():
            symb = '_' + symb.lower()
        result_snake_case += symb
    return result_snake_case
	
def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(string_to_camel_case(input_str()))
output_str(string_to_snake_case(input_str()))
