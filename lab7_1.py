#! /usr/bin/python3
# -*- coding: utf-8 -*-


def string_rotate() -> str:
	""" This function make rotation string"""

	def input_str() -> str:
		""" This function make input of string data"""
		input_string = str(input('Enter your string: '))
		return input_string

	def input_len() -> int:
		""" This function make input of length rotation string"""
		input_length = int(input('Enter your length rotation: '))
		return input_length

	input_string = input_str()
	input_length = input_len()
	
	change_str = ''
	
	if input_length > 0:
		change_str = input_string[input_length:len(input_string)] + input_string[0:input_length]
	elif input_length < 0:
		change_str = input_string[input_length:] + input_string[:input_length]
	else:
		print("Intput length = 0")

	return print(change_str)
string_rotate()
