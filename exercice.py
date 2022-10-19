#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	res = 0

	for letter in text:
		if letter.isalnum():
			res += 1

	return res

def get_word_length_histogram(text):
	res = ''

	for i in text:
		if i == ' ':
			res += i
		elif i.isalnum():
			res += i

	max_length = len(max(res.split(), key = lambda x: len(x)))
	arr = [0] * (max_length + 1)

	for i in res.split():
		arr[len(i)] += 1
		
	return arr


def format_histogram(histogram):
	ROW_CHAR = "*"
	res = ''

	for i in range(1, len(histogram)):
		if i < 10:
			res += ' '
		res += str(i) + ' ' + ROW_CHAR * histogram[i] + '\n'
	
	return res

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	rows = []
	rows.append(LINE_CHAR * len(histogram))
	chart = ''

	for i in range(1, max(histogram) + 1):
		res = ''
		for j in histogram[1:]:
			if j >= i:
				res += BLOCK_CHAR
			else:
				res += ' '
		rows.append(res)

	rows.reverse()

	for i in rows:
		chart += i + '\n'

	print(chart)
	return chart


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
