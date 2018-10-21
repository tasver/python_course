
#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_str() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your string: '))
	return input_string

def string_make_frame(string: str) -> str:
	""" This function make frame string"""
	count_string = len(string)+4
	
	return f'\n{"*"*count_string} \n* {string} * \n{"*"*count_string}'

	
def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(string_make_frame(input_str()))
