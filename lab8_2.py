#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

def input_number() -> list:
	number = input('Enter range of list: ')
	number_list = [i for i in range(1,int(number)+1)]
	random.shuffle(number_list)
	print(number_list)
	return number_list

def merge_sort(alist):
    """print("Splitting ",alist)"""
    if len(alist)>1:
        left_half = alist[:len(alist)//2]
        right_half = alist[len(alist)//2:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        i=0
        j=0
        k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k]=left_half[i]
                i=i+1
            else:
                alist[k]=right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            alist[k]=left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            alist[k]=right_half[j]
            j=j+1
            k=k+1
    """print("Merging ",alist)"""
    return alist


def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    
output_str(merge_sort(input_number()))
