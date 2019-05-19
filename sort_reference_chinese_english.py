#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pypinyin import lazy_pinyin
import argparse
import codecs
import pdb

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--file', type=str, default='',
                    help='path to reference file (each reference per line)')

args = parser.parse_args()
if args.file != '':
	with codecs.open(args.file, mode='r+', encoding='utf-8') as f:
		refs = f.readlines()
elif args.ref != '':
	refs = filter(bool, args.ref.splitlines())
# 
print 'Sort Reference Chinese , English:'
print '*' * 100
refs_ = []
for _ in refs:
	if ord(_[0]) < 128:
		sort_key = u'|'+_.lower()
	else:
		sort_key = ''.join(lazy_pinyin(_)).lower()
	refs_ += [(sort_key, _)]
refs__ = sorted(refs_, key=lambda x: x[0])
for _,r in refs__:
	if r[-1] == u'\n':
		print r,
	else:
		print r