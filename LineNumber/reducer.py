#!/opt/anaconda3/envs/project/bin/python
# -*- coding: UTF-8 -*-
# @Time  : 2019-10-20 20:52:55
# @Author: hackerliang
# @Email : m730026058@mail.uic.edu.hk

# <key>\t<value>
# Mapper: <word, document_name>\t<line_number>
# # Reducer: <word>\t<document_name, [line_number]>

import sys

word_dict = {}

for line in sys.stdin:
    line = line.strip()
    try:
        key, count = line.split('\t')
        (word, file_name) = key.split(',', 1)
    except ValueError:
        continue

    try:
        count = int(count)
    except ValueError:
        word = '---'
        count = 1

    if word in word_dict:
        word_dict[word].append(file_name)
    else:
        word_dict[word] = [file_name]

word_dict = sorted(word_dict.items())

for k, v in word_dict:
    list_dict = dict()
    for i in v:
        for x in eval(i):
            if x in list_dict:
                list_dict[x] += [eval(i)[x]]
                list_dict[x].sort()
            else:
                list_dict[x] = [eval(i)[x]]
    print('%s\t%s' % (k, list_dict))
