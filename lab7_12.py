
#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_number() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your string: '))
	return input_string

def sorted_words(string:str) -> str:
	""" This function deleted spaces"""
	return " ".join(string.split())
	        

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(sorted_words(input_number()))
