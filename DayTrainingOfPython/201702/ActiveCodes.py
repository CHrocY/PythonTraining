#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 生成激活码
# ActiveCodes.py

import random
import string


def make_active_codes(filename, longs=20, times=1000):
	f = open(filename, 'wb')
	char = string.ascii_uppercase + string.digits
	for i in xrange(times):
		result_list = [random.choice(char) for n in xrange(longs)]
		result = ''.join(result_list)
		f.write(result + '\n')
	f.close()
	print "Make Done!"
	return 0


if __name__ == '__main__':
	file_name = 'Active_code.txt'
	long_code = int(raw_input('How long:'))
	time_code = int(raw_input('How much times:'))
	make_active_codes(file_name, long_code, time_code)
