#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_number() -> list:
	""" This function make input of your data"""
	number_step = []
	number_step.append(input('Enter soldiers number: '))
	number_step.append(input('Enter step killing: '))
	return number_step


def killing_soldiers(number_step:list) -> int:
	number, step = number_step
	soldiers = [sold for sold in range(1,int(number)+1)]
	count = int(step)
	iterator = 1
	while len(soldiers) > 1:
		if iterator % count == 0:
			soldiers.pop(0)
		else:
			 next_sold = soldiers.pop(0)
			 soldiers.append(next_sold)
		iterator += 1
	return soldiers[0]

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    
output_str(killing_soldiers(input_number()))
