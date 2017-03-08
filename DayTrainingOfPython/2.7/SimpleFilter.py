#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny


class Filter:
	blocked = []

	def __init__(self, content):
		self.blocked.append(content)

	# 下面这种写法不会接收到任何参数，血的教训～
	# self.blocked = self.blocked.append(content)

	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]


lists = ['ac', 'ca']
f = Filter('ca')
print(f.filter(lists))
