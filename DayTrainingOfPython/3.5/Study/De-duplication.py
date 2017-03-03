#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny
# 探讨一下元素的去重操作


# Method 1:
# 直接用set函数就能达到效果
list_a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8, 9, 0]
set(list_a)

# 这里是一个列表嵌套的列表，注意，它不能用set去重！！！！
list_b = [[1, 2], [2, 3], [2, 3]]
# 为什么不能用set去重呢？因为list_b里面的元素是列表，列表是可变类型，
# 对set来说是unhashable type。打印出list_b中第一个元素的类型：
print(type(list_b[0]))
# 那这里就疑惑了，list_a不是列表吗？它怎么就可以呢？
# 因为对于list_a中的元素来说，它们不是列表，它们是有各自的类型的，比如：
# 它的类型是int
print(list_a[0])

# Summary：对于一个列表来说，组成它的每个元素本身并不一定是列表！它们可以
# 是int、str、list等等，是它们在一起按照列表的组成方式组成了列表这种形式。

# Extention：所以对于copy()和deepcopy()来说，copy()只copy这些组成元素
# 中的不可变类型，可变类型还是copy一个引用，从本质上来说跟用‘=’赋值一样；
# deepcopy()则更像是把里里外外切片一样完全来创造一个新的。


# Method 2:
# 还可以用字典这种方式来实现，虽然这很繁琐、花哨，但它的原理却值得学习！
dict_b = {}
# 把list_a中的元素当做dict_b中的keys传入dict_b中，没值就会默认None。
b = dict_b.fromkeys(list_a)
# 结果很惊讶
b_keys2list = list(b.keys())
print(b_keys2list)

# Summary：之所以能去重，是因为字典的keys是绝对不能重复的！没有谁的身份
# 证号码会一样。同时还要注意一点，字典的keys也是不可变的，我们就靠keys来
# 查找values。正是因为它有这两个特性，所以字典才能是无序的。
