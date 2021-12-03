import sys
from pyspark import SparkContext, SparkConf

spliter = lambda line: line.split(" ")
mword = lambda word: (word, 1)
counter = lambda a,b:a+b

sc = SparkContext("local","word counter app")
words = sc.textFile("./ShamsDaftar1.txt").flatMap(spliter)
words_counter = words.map(mword).reduceByKey(counter)
words_counter.saveAsTextFile("./output/")

