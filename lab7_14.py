#! /usr/bin/python3
# -*- coding: utf-8 -*-
import re

def input_email() -> str:
	""" This function make input of your email"""
	input_string = input('Enter your email: ')
	return input_string
	
def check_email(input_string:str) -> str:
	""" This function checked email"""
	if_is_correct = re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,10}$", input_string)
	if if_is_correct:
	    return 'your email is correct'
	else:
	    return 'your email is not correct'
	

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    

output_str(check_email(input_email()))
