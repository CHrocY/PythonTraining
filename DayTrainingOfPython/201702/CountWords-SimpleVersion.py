#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 任一个英文的纯文本文件，统计其中的单词数


import re


def count_words(filename):
	f = open(filename, 'rb').read()
	words = re.findall(r'[\w]+', f)
	print len(words)
	return 0


if __name__ == '__main__':
	file_name = 'Wind Sand and Stars.txt'
	count_words(file_name)
