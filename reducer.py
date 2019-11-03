#!/opt/anaconda3/envs/project/bin/python
# -*- coding: UTF-8 -*-
# @Time  : 2019-10-20 20:52:55
# @Author: hackerliang
# @Email : m730026058@mail.uic.edu.hk

# <key>\t<value>
# Mapper: <word, document_name>\t<line_number>
# # Reducer: <word, document_name>\t<[line_number]>

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

#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file mapper.py -mapper "python mapper.py" -file reducer.py -reducer "python reducer.py" -input /user/uic/py_wc_input/* -output /user/uic/py_wc_output/
# hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -D mapreduce.reduce.map.memory.mb=5120 -D mapreduce.reduce.memory.mb=5120 -file mapper.py -mapper "python mapper.py" -file reducer.py -reducer "python reducer.py" -input /user/uic/wc_big_files_input/* -output /user/uic/wc_big_files_output_py_mr/