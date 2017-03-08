#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny


# class _singleton(object):
# 	class ConstError(TypeError):
# 		pass
#
# 	def __setattr__(self, name, value):
# 		if name in self.__dict__:
# 			raise self.ConstError
# 		self.__dict__[name] = value
#
# 	def __delattr__(self, name):
# 		if name in self.__dict__:
# 			raise self.ConstError
# 		raise NameError
#
#
# import sys
#
# sys.modules[__name__] = _singleton

class My_Singleton(object):
	def foo(self):
		pass

my_singleton = My_Singleton()


if __name__ == '__main__':
	My_Singleton()