#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 将激活码储存在MySQL数据库中，并提供查询功能


import mysql.connector
import ActiveCodes


def write_to_mysql(filename):
	conn = mysql.connector.connect(user='root', password='cheny',
	                               host='127.0.0.1', database='test')
	cursor = conn.cursor()
	cursor.execute('DROP TABLE IF EXISTS user')
	cursor.execute('create table user(id varchar(20) primary key,  name varchar(20))')
	f = open(filename, 'r').readlines()
	for num, line in zip(xrange(1, len(f) + 1), f):
		line = line[:-1]
		cursor.execute('insert into user(id, name) '
		               'values (%s, %s)',
		               (str(num), line))
		conn.commit()
	cursor.close()
	print 'Write Done!'
	return 0


def read_to_mysql():
	keys = int(raw_input('Search Active code:'))
	conn = mysql.connector.connect(user='root', password='cheny',
	                               host='127.0.0.1', database='test')
	cursor = conn.cursor()
	cursor.execute('select name from user where id = %s', (keys,))
	values = cursor.fetchall()
	print values
	cursor.close()
	conn.close()
	return 0


if __name__ == '__main__':
	ActiveCodes.make_active_codes('my_active_codes.txt')
	write_to_mysql('my_active_codes.txt')
	read_to_mysql()
