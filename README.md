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
