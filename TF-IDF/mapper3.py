#!/opt/anaconda3/envs/project/bin/python
# -*- coding: UTF-8 -*-
# @Time  : 2019-10-20 22:30:15
# @Author: hackerliang
# @Email : m730026058@mail.uic.edu.hk

# <key>\t<value>
# Mapper1: <word, document_name>\t<1>
# Reducer1: <word, document_name>\t<word_appears_time_in_same_document> Get TF Numerator
# Mapper2: <document_name>\t(word, word_appears_time_in_same_document))
# Reducer2: <word, document_name>\t<word_appears_time_in_same_document, total_words_in_this_document> Get TF Denominator
# # Mapper3: <word>\t<document_name, word_appears_time_in_same_document, total_words_in_this_document, 1>
# Reducer3: <word, document_name>\t<TF-IDF> Get TF-IDF

import sys

for line in sys.stdin:
    line = line.strip()
    (key, value) = line.split('\t', 1)
    (word, document_name) = key.split(',', 1)
    (word_appears_time_in_same_document, total_words_in_this_document) = value.split(',', 1)
    print('{}\t{},{},{},{}'.format(word, document_name, word_appears_time_in_same_document, total_words_in_this_document, 1))
