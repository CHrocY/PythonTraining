#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny


class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1

	def __next__(self):
		"""实现了__next__方法，对象就是迭代器咯！"""
		self.a, self.b = self.b, self.a + self.b
		print('use next')  # 查看它们的调用顺序
		return self.b

	def __iter__(self):
		"""只要有__iter__方法，这个Fibs实例化的对象就能迭代～！
		“可迭代”和“是迭代器”是有差别的。比如新建一个列表，自带
		__iter__方法，但是它并不自带__next__方法。"""
		print('use iter')  # 查看它们的调用顺序
		return self

print(dir(Fibs))  # 多了__iter__和__next__方法
f = Fibs()
for i in f:
	if i > 100:
		break
	print(i, '\r\n')