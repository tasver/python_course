#! /usr/bin/python3
# -*- coding: utf-8 -*-

def input_data() -> float:
	""" This function make input text"""
	input_data = (input('Enter your float number: ' ))
	return float(input_data)

def numbers_to_letters(number: float) -> str:
    if number >=1000000: 
        raise ValueError('Not supporter equal or over million')
    numbers = {1: 'один', 2: 'два', 3: 'три', 4: 'чотири', 5: 'п\'ять', 
    6: 'шість', 7: 'сім', 8: 'вісім', 9: 'дев\'ять', 10: 'десять', 
    11: 'одинадцять', 12: 'дванадцять', 13: 'тринадцять', 14: 'чотирнадцять', 
    15: 'п\'ятнадцять', 16: 'шістнадцять', 17: 'сімнадцять', 18: 'вісімнадцять',
    19: 'дев\'ятнадцять',20: 'двадцять', 30: 'тридцять', 40: 'сорок', 
    50: 'п\'ятдесят', 60: 'шістдесят', 70: 'сімдесять', 80: 'вісімдесять', 
    90: 'дев\'яносто', 100: 'сто',200: 'двісті', 300: 'триста', 
    400: 'чотириста', 500: 'п\'ятсот', 600: 'шістсот',700: 'сімсот',
    800: 'вісімсот', 900: 'дев\'ятсот', 0: ''}
    letters_numbers = list()
    number_without_coins = int(number)
    number=list(str(int(number*100)))
    coins_list = number[-2:]
    del number[-2:]
    len_int_number = len(number)
    dozens_thousend=0
    dozens=0
    """thousand"""
    if len_int_number==6:
        hundret_thousend = number_without_coins//100000
        letters_numbers.append(numbers[int(hundret_thousend)*100])
        number_without_coins=number_without_coins-hundret_thousend*100000
        len_int_number=len(str(number_without_coins))
    if len_int_number==5:
        dozens_thousend = number_without_coins//10000
        if dozens_thousend>1:
            letters_numbers.append(numbers[int(dozens_thousend)*10])
        number_without_coins=number_without_coins-dozens_thousend*10000
        len_int_number=len(str(number_without_coins))
    if len_int_number==4:
        units_thousend = number_without_coins//1000
        if dozens_thousend==1:
            letters_numbers.append(numbers[int(dozens_thousend)*10+int(units_thousend)])
            units_thousend=10000+units_thousend
        else:
            letters_numbers.append(numbers[int(units_thousend)])
        number_without_coins=number_without_coins-units_thousend*1000
        len_int_number=len(str(number_without_coins))
    
        if int(units_thousend)==1:
            if "один" in letters_numbers:
                letters_numbers[letters_numbers.index("один")] = "одна"
                letters_numbers.append("тисяча")
        elif 1<int(units_thousend)<5:
            if "два" in letters_numbers:
                letters_numbers[letters_numbers.index("два")] = "дві"
            letters_numbers.append("тисячі")
        elif int(units_thousend)>5:
            letters_numbers.append("тисяч")
        else: letters_numbers.append("тисяч")

    """units+hryvna"""  
    if len_int_number==3:
        hundret = number_without_coins//100
        letters_numbers.append(numbers[int(hundret)*100])
        number_without_coins=number_without_coins-hundret*100
        len_int_number=len(str(number_without_coins))
    if len_int_number==2:
        dozens = number_without_coins//10
        if dozens >2:
            letters_numbers.append(numbers[int(dozens)*10])
        number_without_coins=number_without_coins-dozens*10
        len_int_number=len(str(number_without_coins))
    if len_int_number==1:
        units= number_without_coins//1
        if dozens==1:
            letters_numbers.append(numbers[int(dozens)*10+int(units)])
            units=10+units
        else:
            letters_numbers.append(numbers[int(units)])
        number_without_coins=number_without_coins-units
        len_int_number=len(str(number_without_coins))
    
    if int(units)==1:
        if "один" in letters_numbers:
            letters_numbers[letters_numbers.index("один")] = "одна"
            letters_numbers.append("гривня")
    elif 1<int(units)<5:
        if "два" in letters_numbers:
            letters_numbers[letters_numbers.index("два")] = "дві"
        letters_numbers.append("гривні")
    else: 
        letters_numbers.append("гривень") 
        
    """coins"""
    coins_dozens = coins_list.pop(0)
    coins_units = coins_list.pop(0)
    coins=int(coins_dozens)*10+int(coins_units)
    letters_numbers.append(coins)
    if coins > 10 and coins < 20: 
        letters_numbers.append("копійок")
    elif coins % 10 > 1 and coins % 10 < 5: 
        letters_numbers.append("копійки")
    elif coins % 10 == 1: 
        letters_numbers.append("копійка")
    else: 
        letters_numbers.append("копійок")
    letters_numbers=" ".join(map(str,letters_numbers)).capitalize()
    return str(letters_numbers)
    
def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    
output_str(numbers_to_letters(input_data()))
