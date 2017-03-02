#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Cheny
# 平常都是使用%这种方式格式化输出，简单的打印没什么问题，不过相对新的format，
# 那是要功能差一些。format有如下的优点：
#       1.不需要理会数据类型，这简直太好了；
#       2.可以直接指定名字，这样就可以顺序不同、多次出现；
#       3.填充方式丰富，比如列表、字典都可以填充上去，对齐也更强大；
# 跟%方式一样，format在打印的字符串中使用{}作为标识符，而上面所说的功能就
# 在{}中实现。


# 基本方式，跟%方式很类似，其实如果按顺序来{}中也可以不填充数字，自动的0\1\2\3...
print("Hello {0}, I'a {1}.").format('Li', 'Chen')

# 直接指定，不按照顺序、多次出现这些功能就是这样实现的，'%'可不能这样。
print("Hello {name1}, I'm {name2}.".format(name1='Li',
                                           name2='Chen'))

# 下标填充，在{}还可以通过列表下标来指定填充，不过这看起来有点花哨～
names_list = ['Li', 'Chen']
print("Hello {names[0]}, I'm {names[1]}.".format(names=names_list))

# 字典填充，跟列表很类似
names_dict = {'name': 'Li', 'name2': 'Chen'}
print("Hello {names[name]}  I'a {names[name2]}.".format(names=names_dict))

# Note：字典填充的时候，value的调用跟的时候，key不需要引号。

# Summary:后面3种方式的填充，才体现了format更先进的功能。它们本质上都是使用键值
# 对这种方式来指定填充。

# Extention：
# a)还有一些更花哨的方式，比如通过对象的属性，或者使用魔法参数*args、**kwargs等
# 方式填充。
# b)同时还有格式转化(针对数字)。
# c)对齐和填充。这些不常用、需要大量记忆的内容等需要的时候再来学习！
