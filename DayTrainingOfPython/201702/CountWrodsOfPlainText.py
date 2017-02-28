#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re
import glob
from collections import Counter
from datetime import datetime


def article_analysis(article):
	"""提取纯英语文章中的单词并统计次数"""
	doc = open(article, 'r').read()
	doc_lower = doc.lower()
	doc_re = re.findall(r'[[a-zA-Z]+', doc_lower)
	if not doc_re:
		return [('None', 0)]
	doc_count = Counter(doc_re).most_common(1)
	return doc_count


def sort_dictdata():
	"""搜寻文件夹下的txt文件，并把经过处理的文件排序打印"""
	articles = glob.glob('*.txt')
	f = open('result.txt', 'a')
	for article_m in articles:
		most_times_words = article_analysis(article_m)
		f.write('%s == %s -- %s' % (article_m, most_times_words[0][0], most_times_words[0][1]) + '\n')
	f.close()


if __name__ == '__main__':
	start = datetime.now()
	sort_dictdata()
	stop = datetime.now()
	print stop - start
