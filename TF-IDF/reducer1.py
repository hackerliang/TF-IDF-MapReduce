#!/opt/anaconda3/envs/project/bin/python
# -*- coding: UTF-8 -*-
# @Time  : 2019-10-20 20:51:30
# @Author: hackerliang
# @Email : m730026058@mail.uic.edu.hk

# <key>\t<value>
# Mapper1: <word, document_name>\t<1>
# # Reducer1: <word, document_name>\t<word_appears_time_in_same_document> Get TF Numerator
# Mapper2: <document_name>\t<word, word_appears_time_in_same_document>
# Reducer2: <word, document_name>\t<word_appears_time_in_same_document, total_words_in_this_document> Get TF Denominator
# Mapper3: <word>\t<document_name, word_appears_time_in_same_document, total_words_in_this_document, 1>
# Reducer3: <word, document_name>\t<TF-IDF> Get TF-IDF

# ##
# hadoop jar /path/to/hadoop-streaming-*.jar -D mapreduce.reduce.map.memory.mb=5120
# -D mapreduce.reduce.memory.mb=5120 -D mapreduce.job.reduces=1 -file mapper1.py -mapper "python mapper1.py"
# -file reducer1.py -reducer "python reducer1.py" -input /path/to/input_dir
# -output /path/to/tf-idf_step1/output_dir
# ##

import sys

word_count = 0
word = None
document_name = None
old_word = None
old_document_name = None

for line in sys.stdin:
    (key, value) = line.split('\t', 1)
    (word, document_name) = key.split(',', 1)

    if word == '':
        continue

    if old_word != word or old_document_name != document_name:
        if old_word and old_document_name:
            print('{},{}\t{}'.format(old_word, old_document_name, word_count))
            word_count = 0
        old_word = word
        old_document_name = document_name
    try:
        word_count += int(value)
    except ValueError:
        continue

if word and document_name is not None:
    print('{},{}\t{}'.format(word, document_name, word_count))
