#!/opt/anaconda3/envs/project/bin/python

import sys

word_dict = {}

for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t')
    except ValueError:
        word = '---'
        count = 1

    try:
        count = int(count)
    except ValueError:
        continue

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict.setdefault(word, 1)

word_dict = sorted(word_dict.items())

for k, v in word_dict:
    print('%s\t%s' % (k, v))

#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -file mapper.py -mapper "python mapper.py" -file reducer.py -reducer "python reducer.py" -input /user/uic/py_wc_input/* -output /user/uic/py_wc_output/
#mr-jobhistory-daemon.sh start historyserver