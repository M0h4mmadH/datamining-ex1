import sys
from pyspark import SparkContext, SparkConf

spliter = lambda line: line.split(" ")
mword = lambda word: (word, 1)
counter = lambda a,b:a+b

