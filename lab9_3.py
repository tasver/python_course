#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

def input_data() -> list:
	""" This function make input text"""
	input_data = (input('enter yuour text '))
	return input_data

def change(input_data:str)-> str:
	""" This function change text to morze"""
	dict_input = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.",
	"G":"--.","H":"....","I":"..","J":"-.-.","K":"-.-","L":".-..","M":"--",
	"N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
	"U":"..-","V":"...-","W":".--","X":".-..","Y":"-.--","Z":"--.."}

	crypto = ''.join([dict_input.get(c.upper(), ' ') for c in input_data])

	return crypto
	
def output_str(string:str) -> str:
    """ This function print result"""
    print(string)

output_str(change(input_data()))
