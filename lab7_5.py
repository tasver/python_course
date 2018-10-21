
#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_str() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your string: '))
	return input_string

def string_count_loud(string: str) -> str:
	""" This function make count loud string"""
	loud_letter = ('a', 'o', 'u', 'i', 'e', 'y')
	string = string.lower()
	numbers = [string.count(i) for i in loud_letter]
	numbers = sum(numbers)
	return str(numbers)

	
def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(string_count_loud(input_str()))
