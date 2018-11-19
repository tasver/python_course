#! /usr/bin/python3
# -*- coding: utf-8 -*-
import math

class Dot:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def distance(self, dot_second:float):
        return math.sqrt((dot_second.x - self.x) ** 2 + (dot_second.y - self.y) ** 2)

class Triangle:
    def __init__(self, first_dot, second_dot, third_dot):
        self.first_dot = first_dot
        self.second_dot = second_dot
        self.third_dot = third_dot
        self.first_side = self.first_dot.distance(self.second_dot)
        self.second_size = self.second_dot.distance(self.third_dot)
        self.third_size = self.third_dot.distance(self.first_dot)

    def is_exist(self) -> bool:        
        if self.first_side>0 and self.second_size>0 and self.third_size>0:
            hypot = max(self.first_side, self.second_size, self.third_size)
            cathet = self.first_side + self.second_size + self.third_size - hypot
            if (cathet > hypot):
                return True
            else: False
        else: False

    def get_perimeter(self) -> float:
        if not(self.is_exist()): raise Exception("Triangle not exists")
        return self.first_side + self.second_size + self.third_size

    def get_square(self) -> float:
        if not(self.is_exist()): raise Exception("Triangle not exists")
        p = self.get_perimeter() / 2
        return (p * (p - self.first_side) * (p - self.second_size) * (p - self.third_size)) ** 0.5

def input_data() -> Triangle:
    first_dot = Dot(float(input("Enter A_x: ")), float(input("Enter A_y:  ")))
    second_dot = Dot(float(input("Enter B_x: ")), float(input("Enter B_y: ")))
    third_dot = Dot(float(input("Enter C_x: ")), float(input("Enter C_y: ")))
    return Triangle(first_dot, second_dot, third_dot)

def output(triangle) -> None:
    try:
        print("Perimeter of triangle:", triangle.get_perimeter())
        print("Squere of triangle:", triangle.get_square())
    except:
        print("Triangle exists:", triangle.is_exist())

output(input_data())
