
#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_number() -> int:
	""" This function make input of string data"""
	input_string = str(input('Enter your number: '))
	return int(input_string)

def string_fizz_buzz(number:int) -> str:
	""" This function make fizz or buzz string"""
	result_string = str()
	if number>=100:
	    return "out of range(you enter number >= 100)"
	if number % 3 == 0 and number % 5 == 0:
	    return "Fizz" + "Buzz"
	elif number % 3 == 0:
	    return "Fizz"
	elif number % 5 == 0:
	    return "Buzz"
	else: return "no fizz, no buzz"

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(string_fizz_buzz(input_number()))
