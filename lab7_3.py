#! /usr/bin/python3
# -*- coding: utf-8 -*-
def input_str() -> str:
	""" This function make input of your data"""
	input_string = input('Enter your data: ')
	return input_string
	
def choose_brackets(input_string:str) -> str:
    """ This function choose brackets """
    open_brackets = ('(','[','{','<')
    close_brackets = (')',']','}','>')
    all_brackets = str("")
    open_count = 0
    close_count = 0
    for symb in input_string:
        if symb in open_brackets:
            open_count+=1
            all_brackets=all_brackets.join(" "+symb)
            
        if symb in close_brackets:
            close_count+=1
            all_brackets=all_brackets.join(" "+symb)
        else: pass
    return all_brackets.strip()
    
def check_for_corrects_brackets(all_brackets:str) -> str:
    pairs_brackets = ('()','[]','{}','<>')
    not_brackets=str("")
    count=0
    if (len(all_brackets)%2!=0):
        return "NOT OK"
    else: 
        print(all_brackets.strip())
        len_brackets_str = len(all_brackets)
        while len(all_brackets)>0:
            for symb in pairs_brackets:
                if symb in all_brackets:
                    count+=1
                    all_brackets=all_brackets.replace(symb,"")
                    if len(all_brackets) ==0:
                        print(all_brackets)
                        return True
            if len_brackets_str == len(all_brackets):
                break
        return False
        
    return all_brackets
 

def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    

output_str(check_for_corrects_brackets(choose_brackets(input_str())))
