#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import glob
from PIL import Image


def thumbnail_pic(path):
	a = glob.glob(r'*.jpg')
	for x in a:
		name = os.path.join(path, x)
		im = Image.open(name)
		im.thumbnail((1136, 640))
		print (im.format, im.size, im.mode)
		im.save(name, 'JPEG')
	print 'Done!'


if __name__ == '__main__':
	Path = '.'
	thumbnail_pic(Path)
