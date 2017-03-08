#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny
# 更详细的资料：http://stackoverflow.com/questions/136097/
# what-is-the-difference-between-staticmethod-and-classmethod-in-python
# 实际运用的时候才能正在理解为什么有这么不同的方法，先Mark一个。


def foo(x):
	print("executing foo({0})".format(x))


class A(object):
	def __init__(self, x):
		self.x = x

	def foo(self):
		print("executing foo({0}, {1}".format(self, self.x))

	@classmethod
	def class_foo(cls, x):
		print("executing class_foo({0}, {1}".format(cls, x))

	@staticmethod
	def static_foo(x):
		"""With staticmethods, neither self (the object instance) nor
		cls (the class) is implicitly passed as the first argument. """
		print("executing static_foo({0})".format(x))


# 这里需要先将类实例化，不然对于foo函数来说，它是不能正常工作的。
a = A(23)
# The foo is just a function, but when you call a.foo you don't just get
# the function, you get a "partially applied" version of the function
# with the object instance a bound as the first argument to the function.
# foo expects 2 arguments, while a.foo only expects 1 argument.
#
# And a is bound to foo. That is what is meant by the term "bound" below:
print(a.foo)  # <bound method A.foo of <__main__.A object at 0xb7d52f0c>>
a.foo()

# With a.class_foo, a is not bound to class_foo, rather the class A is
# bound to class_foo
print(a.class_foo)  # <bound method type.class_foo of <class '__main__.A'>>

# Here, with a staticmethod, even though it is a method, a.static_foo
# just returns a good 'ole function with no arguments bound. static_foo
# expects 1 argument, and a.static_foo expects 1 argument too.
print(a.static_foo)  # <function static_foo at 0xb7d479cc>

# A.foo(1)会报错
# 它们可以直接调用类，这样也能正常工作。
A.class_foo(1)
A.static_foo(1)

