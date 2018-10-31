#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

def input_data(user:str) -> list:
	""" This function make input text"""
	input_data = (input('Enter {} cards: ' .format(user)))
	return input_data

def generate_dictionary_cards() -> dict:
    """ This function create dictionary cards"""
    all_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
    '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10,'A': 0}
    return all_cards

def generate_pc_cards() -> str:
    """ This function generate pc cards"""
    all_cards=generate_dictionary_cards()
    pc_cards = random.sample(all_cards.keys(), 3)
    return str(pc_cards)

def calculate_score(input_cards:str)-> str:
	""" This function calculate score of points"""
	input_cards = input_cards.replace("'","")
	input_cards = input_cards.replace("[","")
	input_cards = input_cards.replace("]","")
	input_cards = input_cards.replace(",","")
	input_cards = input_cards.split()
	all_cards = generate_dictionary_cards()
	score = sum([all_cards[card] for card in input_cards])
	if 'A' in input_cards:
	    ace_score = 21 - score
	    if ace_score <= 1: score += 1
	    elif ace_score >= 11: score += 11
	return score

def choose_winner(your_score:int,pc_score:int)-> int:
    """ This function choose the winner and print result"""
    if (your_score>pc_score and your_score<= 21) or (pc_score>21 and your_score<=21):
        return [your_score, pc_score, 1]
    elif (pc_score>your_score and pc_score<= 21) or (your_score>21 and pc_score<=21):
        return [your_score, pc_score, 2]
    elif (your_score == pc_score)and your_score<=21:
        return [your_score, pc_score, 3]
    else: 
        return [your_score, pc_score, 0]
	
def output_str(data:list) -> None:
    """ This function print result"""
    your_score, pc_score, winner = data
    if (your_score> 21):print("Your score is - Bust" )
    else: print("Your score is - {}" .format( your_score))
    if (pc_score> 21):print("Computer score is - Bust" )
    else: print("Computer score is - {}" .format( pc_score))
    if winner==1:
        print("YOU WIN with {} points" .format(your_score))
    elif winner==2:
        print("Computer WIN with {} points" .format(pc_score))
    elif winner==3:
        print("Drow with {} and {} points" .format(your_score, pc_score))
    elif winner==0:
        print("Your and computer are BUSTED")
    else:pass

choose_winner(17, 12)
output_str(choose_winner(calculate_score(input_data('your')),calculate_score(generate_pc_cards())))
