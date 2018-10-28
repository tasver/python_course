#! /usr/bin/python3
# -*- coding: utf-8 -*-

def input_str(input_number:str) -> str:
	""" This function make input of your data"""
	input_string = input("Enter your {} string: ".format(input_number))
	return input_string
	
def count_letters_in_string(input_string:str) -> dict:
	"""This function counting letters """
	letters_count = {}
	for symb in input_string:
		if symb not in letters_count:
			count = input_string.count(symb)
			letters_count.update({symb:count})
	return letters_count

def check_creating_string(dict_first_string:dict,dict_second_string:dict) -> str:
	"""Check if you can create from first string - second"""
	for key, value in dict_second_string.items():
		if key not in dict_first_string:
			return "You can not create string"
		elif value > dict_first_string[key]:
			return "You can not create string"

	return "Congratulatins, you can create this string"



def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    
output_str(check_creating_string(count_letters_in_string(input_str('1')),count_letters_in_string(input_str('2'))))
