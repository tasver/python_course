#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import random

print("Enter 1(scissors) 2(stone) or 3(paper): ")
choice = int(input())
choice_comp = random.randint(1,3)
print(choice,choice_comp)
if (((choice == 1) and  (choice_comp == 2)) or ((choice == 2) and (choice_comp == 3)) or ((choice ==3) and (choice_comp ==1))):
	print("Computer win")
elif (((choice == 1) and (choice_comp == 3)) or ((choice == 2) and (choice_comp == 1)) or ((choice ==3) and (choice_comp ==2))):
	print("You win")
else: print("Drow")


	
