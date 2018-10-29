#! /usr/bin/python3
# -*- coding: utf-8 -*-


def input_number() -> int:
    """This function returns input number"""
    number = input('Enter your number: ')
    return number

def input_rome_number() -> str:
    """This function returns input rome number"""
    number = input('Enter your rome number: ')
    return number

def from_number_to_rome(number:int) -> str:
    """This funtion converted numbers to romes numbers"""
    base = "I"*int(number)
    
    base = base.replace("I"*5, "V")
    base = base.replace("V"*2, "X")
    base = base.replace("X"*5, "L")
    base = base.replace("L"*2, "C")
    base = base.replace("C"*5, "D")
    base = base.replace("D"*2, "M")
    
    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")
    return base
def from_romes_to_number(string:str) ->str:
    """This funtion converted romes numbers to numbers"""
    base = string
    base = base.replace("I", "1 ")
    base = base.replace("V", "5 ")
    base = base.replace("X", "10 ")
    base = base.replace("L", "50 ")
    base = base.replace("C", "100 ")
    base = base.replace("D", "500 ")
    base = base.replace("M", "1000 ")
    
    base = base.replace("CM", "900 ")
    base = base.replace("CD", "400 ")
    base = base.replace("XC", "90 ")
    base = base.replace("XL", "40 ")
    base = base.replace("IX", "9 ")
    base = base.replace("IV", "4 ")
    base = base.strip()
    
    base_result = base.split(" ")
    base_result = list(map(int, base_result))
    base_result=sum(base_result)
    return base_result
    
    
def output_str(string:str) -> None:
    """This function prints numbers"""
    print(string)    
output_str(from_number_to_rome(input_number()))
output_str(from_romes_to_number(input_rome_number()))

