#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import math
import decimal
print("Enter your sallary: ")
sallary = input()

sallary_mill_tax = decimal.Decimal(sallary) * (decimal.Decimal('18')/decimal.Decimal('100'))
sallary_phys_tax = decimal.Decimal(sallary) * (decimal.Decimal('1.5')/decimal.Decimal('100'))
sallary_all = decimal.Decimal(sallary) - decimal.Decimal(sallary_mill_tax) - decimal.Decimal(sallary_phys_tax)
	
print(f"Податок на доходи фізичних осіб 18% = {sallary_mill_tax}") 	
print(f"Військовий збір 1.5% = {sallary_mill_tax}") 
print(f"Зарплата = {sallary_all}") 
