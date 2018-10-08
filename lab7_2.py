#! /usr/bin/python3
# -*- coding: utf-8 -*-
def string_check() -> str:
	""" This function make rotation string"""

	def input_str() -> str:
		""" This function make input of string data"""
		input_string = str(input('Enter your string: '))
		return input_string

	input_string = input_str()
	string_chars = str()
	for i in input_string:
		if i.isalpha():
			string_chars+=i.lower()
		else: continue

	if string_chars[::] == string_chars[::-1]:
		print(True)
	else: print(False)
	
	return print(string_chars)

string_check()
