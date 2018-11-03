#! /usr/bin/python3
# -*- coding: utf-8 -*-
from bitstring import BitArray
from itertools import zip_longest
from operator import sub

def input_data() -> list:
    """ This function make input text"""
    input_data = (input('Enter your text message: '))
    return input_data

def data_to_bytes(input_data:str):

    input_data_bin=input_data.encode('utf-8')
    input_data_binary=0
    string_binary_data=str()
    for x in input_data_bin:
        input_data_binary=x-96
        string_binary_data+=str(input_data_binary)+" "
    print(string_binary_data)
    print(type(string_binary_data))
    return string_binary_data

def file_to_byte(path:str) -> list:    
    with open(path,'rb') as image:
        arr = []
        byte = image.read(1)
        while byte:
            arr.append('{:08b}'.format(ord(byte)))
            byte = image.read(1) 
    count = 0
    arr3=[]    
    for x in arr:
        temp = int(arr[count], 2)
        arr3.append(temp)
        count=count+1 
    count = 0
    return arr3

def crypto_file(string_binary_data:str)->list:
    """ This function crypt data in photo"""
    with open('RAY.BMP','rb') as image:
        arr = []
        byte = image.read(1)
        while byte:
            arr.append('{:08b}'.format(ord(byte)))
            byte = image.read(1) 
    count = 0
    arr3=[]    
    for x in arr:
        temp = int(arr[count], 2)
        arr3.append(temp)
        count=count+1 
    arr5=arr3[0:100]
    arr4=arr3[100:]
    count = 0
    string_binary_data = string_binary_data.split(" ")

    for x in string_binary_data:
        if x.isdigit():
            if arr4[count] < 255-26:
                arr4[count]=int(x)+int(arr4[count])
            else: 
                arr4[count]= int(arr4[count]) - int(x)
            count=count+20
    main_arr=arr5+arr4

    return main_arr

def byte_to_file(iterable, n, fillvalue=None):
    # byte_to_file('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)
 
def crypto_file_into_bytes(main_arr:list)->list:
    arr = []
    for x in main_arr:
        arr.extend('{:08b}'.format(x))
    return arr

def write_file(arr:list) -> None:
    with open('output.bmp', 'wb') as f:
        f.write(bytearray(int(''.join(x),2) for x in byte_to_file(arr, 8)))

def decrypt(crypt:list, nocrypt:list)->str:
    crypt=crypt[100:500]
    nocrypt=nocrypt[100:500]
    text = []
    sub_iter = map(sub, crypt, nocrypt)
    sub_iter = list(filter(None, sub_iter))
    for i in sub_iter:
        i = i+96
        text.append(chr(i))
    text = ''.join(text)
    print(text)

    return print("Your text is - '{}'".format(text))

decrypt(crypto_file(data_to_bytes(input_data())),(file_to_byte("RAY.BMP")))
write_file(crypto_file_into_bytes(crypto_file(data_to_bytes(input_data()))))
