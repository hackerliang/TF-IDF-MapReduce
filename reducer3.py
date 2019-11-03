#!/opt/anaconda3/envs/project/bin/python3
# -*- coding: UTF-8 -*-
# @Time  : 2019-10-20 23:20:10
# @Author: hackerliang
# @Email : m730026058@mail.uic.edu.hk

# <key>\t<value>
# Mapper1: <word, document_name>\t<1>
# Reducer1: <word, document_name>\t<word_appears_time_in_same_document> Get TF Numerator
# Mapper2: <document_name>\t(word, word_appears_time_in_same_document))
# Reducer2: <word, document_name>\t<word_appears_time_in_same_document, total_words_in_this_document> Get TF Denominator
# Mapper3: <word>\t<document_name, word_appears_time_in_same_document, total_words_in_this_document, 1>
# # Reducer3: <word, document_name>\t<TF-IDF> Get TF-IDF

# ##
# hadoop jar /path/to/hadoop-streaming-*.jar -D mapreduce.reduce.map.memory.mb=5120
# -D mapreduce.reduce.memory.mb=5120 -D mapreduce.job.reduces=24 -file mapper2.py -mapper "python mapper2.py"
# -file reducer2.py -reducer "python3 reducer2.py" -input /path/to/tf-idf_step1/output_dir
# -output /path/to/tf-idf_step3/output_dir
# ##

import sys
import math

# You should type your number of document here, in this assignment the value is 224
NUMBER_DOCUMENTS = 224

corpus_word_count = 0
old_word = None
word_statistics_dict = {}
corpus_word_count_dict = {}

for line in sys.stdin:
    line = line.strip()
    (word, val) = line.split('\t', 1)
    values = val.split(',')
    count = values[3]

    if old_word != word:
        if old_word:
            corpus_word_count_dict[old_word] = corpus_word_count
            corpus_word_count = 0
        old_word = word
    corpus_word_count += int(count)
    if word in word_statistics_dict.keys():
        word_statistics_dict[word].append("{},{},{}".format(values[0], values[1], values[2]))
    else:
        word_statistics_dict[word] = list()
        word_statistics_dict[word].append("{},{},{}".format(values[0], values[1], values[2]))

corpus_word_count_dict[old_word] = corpus_word_count

for word in corpus_word_count_dict.keys():
    word_stats_list = word_statistics_dict[word]
    for values in word_stats_list:
        values = values.split(",")
        tf = int(values[1])/int(values[2])
        idf = math.log10(NUMBER_DOCUMENTS / (corpus_word_count_dict[word]))
        tf_idf = tf * idf
        print("{},{}\t{}".format(word, values[0], tf_idf))
