#! /usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image

def input_data() -> list:
	""" This function make input text"""
	input_data = (input('Enter your text message: '))
	return input_data

def crypt_data_in_photo(input_data: str) -> str:
	""" This function crypt data in photo"""
	path = 'RAY.BMP'
	
	image = Image.open(path)
	im = list(image.getdata())
	input_data = input_data.lower()
	input_data_bin=input_data.encode('utf-8')
	input_data_binary=0
	string_binary_data=str()
	for x in input_data_bin:
		input_data_binary=x-96
		string_binary_data+=str(input_data_binary)+" "
	print(input_data_binary)
	print(string_binary_data)

	number_symb = 0

	for x in im:
		r, g, b= image.getpixel((1,1))
		if r<255-26:
			r=r+number_symb
		else:
			r=r-number_symb
	return [r,g,b]



def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(crypt_data_in_photo(input_data()))
