#! /usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
import math

def formula(a:float, b:float)-> float:
	x = (math.sqrt(a*b))/(math.e**a * b) + a * math.e**(2*a/b)
	return x

def output(x:float) -> str:
	print(x)

class tests(unittest.TestCase):

	def test_equal_first(self):
		self.assertEqual(formula(0,1),0.0)

	def test_equal_second(self):
		self.assertAlmostEqual(formula(0.5,10),0.688209837593,7)
		
unittest.main()
