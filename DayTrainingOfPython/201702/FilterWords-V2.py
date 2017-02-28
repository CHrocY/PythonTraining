#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny


def filter_words_list():
	filter_list = []
	with open('FilterWords.txt', 'r') as f:
		for line in f:
			filter_list.append(line.strip())
		return filter_list


def filter_or_not(word, words):
	return word in words


def words_replace(word, words):
	return words.replace(word, '**')


def main(words):
	"""重构后的代码，将每个功能都细分了，如果以后想用哪个
	功能，这里就有分成小模块的功能可用，接口一定要简洁，参
	数也要简单明了，这真是很难兼得。"""
	words_list = filter_words_list()
	for word in words_list:
		if filter_or_not(word, words):
			words = words_replace(word, words)
	return words


if __name__ == '__main__':
	input_words = raw_input("Input your words>>")
	print main(input_words)
