#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny


def filter_words_list():
	"""如果有需要，我在这里还可以写一个add_filter模块，然后把
	这个文本格式写成字典，加快查找速度也是很好的。"""
	filter_list = []
	with open('FilterWords.txt', 'r') as f:
		for line in f:
			filter_list.append(line.strip())
		# 我又在这里犯了错误，把return放在了里面，结果让我排错
		# 了很久，白白浪费了时间，下次一定要记住这个问题，循环
		# 的时候要搞明白它们之间的逻辑关系。
		return filter_list


def words_replace(words):
	f_words_list = filter_words_list()
	for f_word in f_words_list:
		if f_word in words:
			words = words.replace(f_word, '**')
	return words


# 目前这代码的参数可以很简洁了，但是代码的复用性不高，
# 我也该将这些方法分细一点，结果如下：
# filter_words_list：把敏感词文件中的内容转化到列表中
# filter_or_not:判断输入的内容是否含有敏感词部分
# words_replace:将敏感词替换为**
# main:这里的主函数，把上面这些函数组合起来，实现目标功能。
# 不过这样一来，这些函数的参数部分就会显得很复杂了，不过
# 这两者本来就不好得兼。
if __name__ == '__main__':
	input_word = raw_input("Input your words>>")
	print words_replace(input_word)
