#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author = Cheny
# **学习笔记**
# argparse模块可以从sys.argv中解析出参数，可以编写出更友好的命令行接口

import os
import sys
import argparse
from chardet.universaldetector import UniversalDetector

# 创建一个ArgumentParser对象，它会保存从命令行解析成Python数据类型所需的所有信息
parser = argparse.ArgumentParser(description='文本文件编码检测与转换')
# 通过ArgumentParser对象调用它的方法add_argument()添加脚本的参数信息到自身
# nargs='+'表示所有命令行参数都被收集到一个列表中，跟正则表达式中'+'类似，至少
# 需要1个参数，这里很容易理解，我们至少需要放入一个文件呀！nargs还可以有其他的参
# 数，详细的查看文档
parser.add_argument('filePaths', nargs='+',
                    help='检测或转换文件路径')
# 因为在后面的代码，如果不输入参数，就默认的转换为UTF-8，所以这里使用nargs='?',也
# 跟正则表达式中类似，可以有一个参数，也可以没有任何参数，没有我也不报错;因为我们
# 这里nargs='?',所以后面可以多一个const='UTF-8'来设置默认值
parser.add_argument('-e', '--encoding', nargs='?', const='UTF-8',
                    help=u'''
                    支持的编码有：
ASCII, (缺省) UTF-8 (with or without a BOM), UTF-16 (with a BOM),
UTF-32 (with a BOM), Big5, GB2312/GB18030, EUC-TW, HZ-GB-2312, ISO-2022-CN,
EUC-JP, SHIFT_JIS, ISO-2022-JP,ISO-2022-KR, KOI8-R, MacCyrillic, IBM855,
IBM866, ISO-8859-5, windows-1251, ISO-8859-2, windows-1250, EUC-KR,
ISO-8859-5, windows-1251, ISO-8859-1, windows-1252, ISO-8859-7, windows-1253,
ISO-8859-8, windows-1255, TIS-620
                    ''')
# 这里'-o', '--output'都可以在后面来调用，跟上面的'-e'之类的一样的效果，其实它们
# 一会都会被argparse模块解析成相应的参数供下面使用
parser.add_argument('-o', '--output',
                    help='输出目录')
# 解析ArgumentParser通过add_argument添加的参数，得到一个Namespace对象
# 后面用到的args.encoding、args.output都是出自于它的解析出的参数
args = parser.parse_args()
# 输出目录不为空就视为开启转换，若未指定转换编码，就默认转换为UTF-8
if args.output is not None:
	if not args.encoding:
		# 默认使用UTF-8编码
		args.encoding = 'UTF-8'
	# 检测用户提供的输出目录是否有效
	if not os.path.isdir(args.output):
		print('Invalid Directory:' + args.output)
		sys.exit()
	else:
		if args.output[-1] != '/':
			args.output += '/'
# 实例化一个通用检测器
detector = UniversalDetector()
print()
print('Encoding (Confidence)', ':', 'File path')
for filePath in args.filePaths:
	# 检测文件路径是否有效，无效就跳过
	if not os.path.isfile(filePath):
		print('Invalid Path:' + filePath)
		continue
	# 重置检测器
	detector.reset()
	# 这里需要用二进制模式，换行符一类
	for each in open(filePath, 'rb'):
		# 检测器读取数据
		detector.feed(each)
		# 若检测完成则跳出循环
		if detector.done:
			break
	# 关闭检测器
	detector.close()
	# 读取结果
	charEncoding = detector.result['encoding']
	confidence = detector.result['confidence']
	# 打印信息
	if charEncoding is None:
		charEncoding = 'Unknown'
		confidence = 0.99
	print('{} {:>12} : {}'.format(charEncoding.rjust(8),
	                              '(' + str(confidence * 100) + '%)', filePath))
	if args.encoding and charEncoding != 'Unknown' and confidence > 0.6:
		# 若未设置输出目录则覆盖源文件
		outputPath = args.output + os.path.basename(filePath) if args.output else filePath
		with open(filePath, 'r', encoding=charEncoding, errors='replace') as f:
			temp = f.read()
		with open(outputPath, 'w', encoding=args.encoding, errors='replace') as f:
			f.write(temp)
