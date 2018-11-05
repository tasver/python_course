#! /usr/bin/python3
# -*- coding: utf-8 -*-
def parse_nginx(name_file: str) ->int:
	with open(name_file,'r') as file:
		for line in file:
			yield line.split()[9]

a = parse_nginx('2017_05_07_nginx.txt')
count_bytes = 0
for i in a:
	i = int(i)
	count_bytes +=i
print(count_bytes)
