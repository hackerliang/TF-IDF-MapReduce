#!/opt/anaconda3/envs/project/bin/python
# -*- coding: UTF-8 -*-
# @Time  : 2019-10-20 20:41:55
# @Author: hackerliang
# @Email : m730026058@mail.uic.edu.hk

# <key>\t<value>
# # Mapper: <word, document_name>\t<line_number>
# Reducer: <word, document_name>\t<[line_number]>

import os
import re
import sys

file_path = os.getenv('mapreduce_map_input_file')
file_name = os.path.split(file_path)[-1]

countLine = 1
for line in sys.stdin:
    line_dict = dict()
    line = line.strip()
    words = line.split()
    line_dict[file_name] = countLine
    for word in words:
        print("%s,%s\t%s" % (re.compile("[^a-zA-Z]").sub("", word).lower(), line_dict, 1))
    countLine += 1
