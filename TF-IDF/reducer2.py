#!/opt/anaconda3/envs/project/bin/python
# -*- coding: UTF-8 -*-
# @Time  : 2019-10-20 21:30:10
# @Author: hackerliang
# @Email : m730026058@mail.uic.edu.hk

# <key>\t<value>
# Mapper1: <word, document_name>\t<1>
# Reducer1: <word, document_name>\t<word_appears_time_in_same_document> Get TF Numerator
# Mapper2: <document_name>\t(word, word_appears_time_in_same_document))
# # Reducer2: <word, document_name>\t<word_appears_time_in_same_document, total_words_in_this_document> Get TF Denominator
# Mapper3: <word>\t<document_name, word_appears_time_in_same_document, total_words_in_this_document, 1>
# Reducer3: <word, document_name>\t<TF-IDF> Get TF-IDF

# ##
# hadoop jar /path/to/hadoop-streaming-*.jar -D mapreduce.reduce.map.memory.mb=5120
# -D mapreduce.reduce.memory.mb=5120 -D mapreduce.job.reduces=1 -file mapper2.py -mapper "python mapper2.py"
# -file reducer2.py -reducer "python reducer2.py" -input /path/to/tf-idf_step1/output_dir
# -output /path/to/tf-idf_step2/output_dir
# ##

import sys

total_words_in_this_document = 0
old_document_name = None
doc_words = {}
total_words_in_this_document_aggregate = {}
value = []

for line in sys.stdin:
    line = line.strip()
    (document_name, value) = line.split('\t', 1)
    (word, word_count) = value.split(',', 1)

    if old_document_name != document_name:
        if old_document_name:
            total_words_in_this_document_aggregate[old_document_name] = total_words_in_this_document
            total_words_in_this_document = 0
        old_document_name = document_name
    try:
        total_words_in_this_document += int(word_count)
        if document_name in doc_words.keys():
            temp_list = doc_words[document_name]
            temp_list.append('{}\t{}'.format(word, word_count))
            doc_words[document_name] = temp_list
        else:
            temp_list = list()
            temp_list.append('{}\t{}'.format(word, word_count))
            doc_words[document_name] = temp_list
    except ValueError:
        continue

total_words_in_this_document_aggregate[old_document_name] = total_words_in_this_document

for key in doc_words.keys():
    contents = doc_words[key]
    for content in contents:
        content = content.rstrip()
        (word, word_count) = content.split("\t", 1)
        print('{},{}\t{},{}'.format(word, key, word_count, total_words_in_this_document_aggregate[key]))
