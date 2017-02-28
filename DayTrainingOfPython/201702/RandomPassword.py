#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 这是我尝试使用import方法的产物

import ActiveCodes

# passwd_len = int(raw_input('How long:'))
# char = string.digits + string.ascii_letters
# # 下面这个推导式会返回一个列表
# result = [random.choice(char) for i in xrange(passwd_len)]
# print ''.join(result)
"""想来想去，我干脆试试这种魔法一般的方法吧~可以直接导入写好的模块哟~"""
ActiveCodes.make_active_codes('my_active_codes.txt')
