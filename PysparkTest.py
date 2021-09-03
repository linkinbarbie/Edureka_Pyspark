# testing RDD
from typing import List, Union, Tuple, Dict, Optional, Any

import pyspark
from pyspark.sql import *
from pyspark.sql.functions import explode

sc = pyspark.SparkContext.getOrCreate()  # set up the spark context for this jvm

# SparkSession 1
spark = SparkSession \
    .builder \
    .getOrCreate()
print(spark)
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5, 6, 7])
print("RDD count" + str(rdd.count()))

# Spark session internally creates a sparkContext variable of SparkContext
# note you can use newSession() or builder to create your spark session

# Pyspark RDD(Resilient Distributed Dataset) is a fundamental data structure concept in Spark
# it is fault tolerant
# immutable distributed collections of objects i.e. once you create an RDD you cannot change it
# Each dataset in RDD is divided into logical partitions,
# which can be computed on different nodes of the cluster.

# You can only create one SparkContext per jvm - if you want to create a new
# SparkContext you haven to use stop()

spark = SparkSession \
    .builder \
    .getOrCreate()

# using parallelize
dataList = [("Java", 2000), ("Python", 30000), ("Scala", 6000)]
rdd = spark.sparkContext.parallelize(dataList)
print(rdd.count())
# this means that each of this tuple will be processed on different nodes of the cluster

# using textFile()
data = sc.textFile(
    "C:\\Users\\linki\\Spark\\spark-3.1.2-bin-hadoop3.2\\spark-3.1.2-bin-hadoop3.2\\pnaptest2.txt")  # RDD for text data

# after you create an RDD you can perform transformations/actions on your RDD
# flatMap is a transformation  - this step works for textFile
data2 = data.flatMap(lambda x: x.split(" "))  # splits the data in the texFile RDD by space delimiter
for i in data2.collect():  # makes it possible to iterate by placing the data into a list format
    print(i)

arrayData = [('Barbara Aghanenu', ['Java', 'Scala'], {'hair': 'black', 'eye': 'brown'}),
             ('Anibal Postala', ['Python', 'Scala'], {'hair': 'blond', 'eye': None}),
             ('Viral Vyas', None, None),
             ('Leslie Whu', ['C#', 'R'], {})]
df = spark.createDataFrame(arrayData, ['name', 'knownLangs', 'properties'])
df.printSchema()
df.show()
df2 = df.select(df.name,explode(df.knownLangs))
df2.printSchema()
df2.show()
# RDD Transformations Transformations on Spark RDD returns another RDD and transformations are lazy meaning they
# don’t execute until you call an action on RDD. Some transformations on RDD’s are flatMap(), map(), reduceByKey(),
# filter(), sortByKey() and return new RDD instead of updating the current.

# flatMap()


#
# RDD Actions
# RDD Action operation returns the values from an RDD to a driver node. In other words, any RDD function that returns non RDD[T] is considered as an action.
#
# Some actions on RDD’s are count(), collect(), first(), max(), reduce() and more.
