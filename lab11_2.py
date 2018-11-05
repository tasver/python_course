#! /usr/bin/python3
# -*- coding: utf-8 -*-

def input_data() -> str:
    """ This function make input number"""
    input_data = (input('Enter your number: '))
    
    if len(input_data)>6:
    	print("Too long number")
    return input_data
def input_count() -> str:

	input_count = (input('Enter count: '))
	return input_count

def reverse_and_multiple(input_number:str,input_count:str)->str:

	while int(input_count)>0:		
		reverse_number = input_number[3:] + input_number[0:3]
		multiple_number =  int(reverse_number)*int(input_number)
		result_str = ((12-len(str(multiple_number)))*"0")+str(multiple_number)
		result = result_str[3:9]
		input_number = result
		input_count=int(input_count)-1
		yield result
def output_str(input_count:str) -> str:
    """ This function print result"""
    a = reverse_and_multiple(input_data(),input_count)
    input_count= int(input_count)
    while input_count>0:
    	print(int(next(a)))
    	input_count=input_count-1

output_str(input_count())
