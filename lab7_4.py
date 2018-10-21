
#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_str() -> str:
	""" This function make input of string data"""
	input_string = str(input('Enter your string: '))
	return input_string

def string_crypt(string: str) -> str:
	""" This function make crypt string"""
	result_string = str()
	string = string.lower()
	for symb in string:
	    result_string += chr(ord(symb) + 1)
	return result_string
	
def string_check_crypt(check_str:str) -> str:
    """ this funtion checking out of range crypt """
    check_str = check_str.replace("{","a")
    check_str = check_str.replace("ѐ","а")
    print(check_str)
    return check_str
	
def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(string_check_crypt(string_crypt(input_str())))
