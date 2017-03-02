#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

"""
实现想法：
  我先设置一个字典，其中IP作为键， 出现的次数作为值。然后
我把列表中的IP都拿去跟下面字典中的键对比，没有的就添加到字
典中，并把次数写为1，有的话，就将次数+1。当然，从开始的时候
是一个空字典，第一次出现的自然是直接添加到字典中，但要是下次
再出现，那么就是在对于键的值中加1。然后结束的时候找到字典中
值最大的，然后打印出相应的键就行了。
  这里尽量与字典靠齐，也是因为字典比列表高效很多。不过这只
是我具体的做法，完全是属于重复造轮子。python中这类方法早就有
解决这类方法的模块了。只需要调用一下，简单还比我的高效。
"""

lists = ['10.199.88.161',
         '10.199.88.162',
         '10.199.88.163',
         '10.199.88.163',
         '10.199.88.163']
dicts = {}
for i in lists:
	if i not in dicts.keys():
		dicts[i] = 1  # 从来没有出现过就添加键值对
	else:
		dicts[i] += 1  # 已经有了就更新键值对，其值+1
for n in dicts.keys():
	if dicts[n] == max(dicts.values()):  # max是很好用，找出最大的值
		print(u'出现次数最多的IP是：', n)

# 这个是使用内置方法的版本，明显太快了。
words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]
r = Counter(words).most_common(1)
print(u'出现次数最多的单词是：%s, 出现了%s次' % (r[0][0], r[0][1]))
