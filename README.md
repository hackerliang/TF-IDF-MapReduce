<img src="https://uicdatascience.com/img/logo.png" align="right" />

# TF-IDF-MapReduce
A python mapreduce script to count TF-IDF base on hadoop mapreduce

****
## Table of contents
* [WordCount](#WordCount)
* [LineNumber](#LineNumber)
* [TF-IDF](#TF-IDF)
    * MapReduce1
    * MapReduce2
    * MapReduce3

### WordCount
>\<key\> \<value\>
>> Mapper: \<word\> \<1\>

>> Reducer: \<word\> \<wordcount\>
```shell
hadoop jar /path/to/hadoop-streaming-*.jar \
-D mapreduce.reduce.map.memory.mb=5120 \
-D mapreduce.reduce.memory.mb=5120 \
-file mapper.py \
-mapper "python mapper.py" \
-file reducer.py \
-reducer "python reducer.py" \
-input /path/to/inputdirs \
-output /path/to/outputdirs
```

### LineNumber
>\<key\> \<value\>
>> Mapper: \<word, document_name\> \<line_number\>

>> Reducer: \<word, document_name\> \<[line_number]\>
```shell
hadoop jar /path/to/hadoop-streaming-*.jar \
-D mapreduce.reduce.map.memory.mb=5120 \
-D mapreduce.reduce.memory.mb=5120 \
-file mapper.py \
-mapper "python mapper.py" \
-file reducer.py \
-reducer "python reducer.py" \
-input /path/to/inputdirs \
-output /path/to/outputdirs
```

### TF-IDF
>\<key\> \<value\>
>>Mapper1: \<word, document_name\> \<1\>

>>Reducer1: \<word, document_name\> \<word_appears_time_in_same_document\>

>>Mapper2: \<document_name\> \<word, word_appears_time_in_same_document\>

>>Reducer2: \<word, document_name\> \<word_appears_time_in_same_document, total_words_in_this_document\>

>>Mapper3: \<word\> \<document_name, word_appears_time_in_same_document, total_words_in_this_document, 1\>

>>Reducer3: \<word, document_name\> \<TF-IDF\>
```shell
hadoop jar /path/to/hadoop-streaming-*.jar \
-D mapreduce.reduce.map.memory.mb=5120 \
-D mapreduce.reduce.memory.mb=5120 \
-file mapper.py \
-mapper "python mapper.py" \
-file reducer.py \
-reducer "python reducer.py" \
-input /path/to/inputdirs \
-output /path/to/outputdirs
```
