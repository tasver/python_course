#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
print("Enter your height(met) and weight(kg): ")
height = float(input())
weight = float(input())
BodyMassIndex = weight / height ** 2
print(f" Your Body Mass Index = {BodyMassIndex}")
