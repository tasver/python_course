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
    number=list(str(int(number*100)))
    coins_list = number[-2:]
    del number[-2:]
    len_int_number = len(number)
    
    if 3<len_int_number<7:
        less_then_thousand = number[-3:]
        more_then_thousand = number[3:]
    else: less_then_thousand = number
    
    
    """hundrets + dozens + units + hryvna"""
    if len(less_then_thousand)==3:
        hundrets = less_then_thousand.pop(0)
        """hundrets"""
        letters_numbers.append(numbers[int(hundrets)*100])
    if 1<len(less_then_thousand)<3:
        dozens = less_then_thousand.pop(0)
        units = less_then_thousand.pop(0)
        
        """dozens+units"""
        if int(dozens)>1:
            letters_numbers.append(numbers[int(dozens)*10])
            letters_numbers.append(numbers[int(units)])
        elif 0<int(dozens)<=1:
            letters_numbers.append(numbers[int(dozens)*10+int(units)])
        elif int(dozens)<1:
            letters_numbers.append(numbers[int(units)])
        else:pass
        """units+hryvna"""
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
    return letters_numbers
    
def output_str(string:str) -> str:
    """ This function print result"""
    print(string)
    
output_str(numbers_to_letters(input_data()))

"""lst = list(str(int(amount * 100)))
    rate = 5
    index = -(rate + 2)
    while lst[index] == '1' and index != -1:
        lst[index] += lst[index + 1]
        lst[index + 1] = '0'
        index += 3
    while len(lst) > rate:
        poped = lst.pop(0)
        sample.append(numbers[int(poped) * 10 ** (len(lst) - len(poped) - rate + 1)])
    if "один" in sample:
        sample[sample.index("один")] = "одна"
        sample.append("тисяча")
    elif "два" in sample:
        sample[sample.index("два")] = "дві"
        sample.append("тисячі")
    else: sample.append("тисяч")
    rate -= 3
    while len(lst) > rate:
        poped = lst.pop(0)
        sample.append(numbers[int(poped) * 10 ** (len(lst) - len(poped) - rate + 1)])
    if "один" in sample:
        sample[sample.index("один")] = "одна"
        sample.append("гривня")
    elif "два" in sample:
        sample[sample.index("два")] = "дві"
        sample.append("гривні")
    else: sample.append("гривень")
    coins = int(''.join(lst))
    sample.append(str(coins))
    if coins > 10 and coins < 20: sample.append("копійок")
    elif coins % 10 > 1 and coins % 10 < 5: sample.append("копійки")
    elif coins % 10 == 1: sample.append("копійка")
    else: sample.append("копійок")
    return ' '.join(' '.join(sample).split()).capitalize()"""
