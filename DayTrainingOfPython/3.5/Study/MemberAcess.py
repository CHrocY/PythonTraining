#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny


class ArithmeticSequence:
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}

	# 使用静态方法，把本来放在类外面的函数放入类中来，
	# 有利于命名空间的整洁和代码的美观～也许吧～
	@staticmethod
	def checkIndex(key):
		if not isinstance(key, int): raise TypeError
		if key < 0: raise IndexError

	def __getitem__(self, key):
		"""返回与所给的key对应的值"""
		ArithmeticSequence.checkIndex(key)
		# 尝试获取值
		try: return self.changed[key]
		# 没有值就计算值
		except KeyError:
			print("Calculate new value")
			return self.start + key*self.step

	def __setitem__(self, key, value):
		"""给这个实例化的类赋值的时候自动调用这个方法"""
		ArithmeticSequence.checkIndex(key)
		self.changed[key] = value
		print(self.changed)

s = ArithmeticSequence(10, 2)  # 初始化一个从10开始，步长为2的实例
print(s[4])  # 询问s[4]这个key的值，只会调用__getitem__方法
s[20] = 1  # 将s[20]这个key的值赋为1，只会调用__setitem__方法