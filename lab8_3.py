#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

def input_number() -> list:
    """This function returns random lists of numbers"""
    number = input('Enter range of number: ')
    number_list=[random.randint(1,int(number)**2)for i in range(1,int(number)+1)]
    random.shuffle(number_list)
    return number_list

def average_median_numbers(number_list: list) -> float:
    """This function returns median of the random list"""
    average_number = (sum(number_list) / len(number_list))
    len_number_list = len(number_list)
    number_list = sorted(number_list)
    if len_number_list%2 == 1:
        median_number =  number_list[len_number_list//2]
    else: 
        median_number = (number_list[len_number_list//2-1] + 
        number_list[len_number_list//2])/2
    return [average_number,median_number,number_list]


def output_str(avg_med_numbers) -> None:
    """This function prints random list, average and median of the list"""
    average_number,median_number,number_list=avg_med_numbers
    print( '\nList of number:', number_list, '\nAverage of numbers:', 
    average_number,'\nMedian of numbers:', median_number )
    
output_str(average_median_numbers(input_number()))
