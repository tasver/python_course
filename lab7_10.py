
#! /usr/bin/python3
# -*- coding: utf-8 -*-
from decimal import Decimal
def input_number() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your string: '))
	return input_string

def search_shortest_word(string:str) -> str:
	""" This function search the shortest word"""
	result_string = str()
	string_split = string.split()
	shortest = 999
	print(string_split)
	for word in string_split:
	    if shortest > len(word):
	        shortest = len(word)
	    else: pass
	return shortest
	        

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(search_shortest_word(input_number()))
