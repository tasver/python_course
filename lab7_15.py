
#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random
def input_number() -> int:
	""" This function make input of number passoword"""
	input_string = str(input('Enter your number of password characters: '))
	return int(input_string)
	
def sorted_words(number:int) -> str:
	""" This function generate password"""
	digits = '1234567890'
	small_letters = 'abcdefghigklmnopqrstuvyxwz'
	upper_letters = 'ABCDEFGHIGKLMNOPQRSTUVYXWZ'
	symbols = '!@#$%^&*'
	password = str()
	if number < 8:
	    return "your password can not be < 8 characters"
	else:
	    for num in range(1,int(number/4)):
	        password += random.choice(digits)
	    for num in range(1,int(number/4)):
	        password += random.choice(symbols)
	    for num in range(1,int((number - len(password))/2)):
	        password += random.choice(small_letters)
	    for num in range(1,int(number - len(password))+1):
	        password += random.choice(upper_letters)
	    if len(password)>number:
	        password = password[0:number]
	password_list = list(password)
	random.shuffle(password_list)
	password = ''.join(password_list)
	    
	    
	return f'your password is - {password} \n lentgh is {len(password)}'
	        

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    

output_str(sorted_words(input_number()))
