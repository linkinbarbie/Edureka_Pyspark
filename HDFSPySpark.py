import pyspark
from pyspark.sql import *
from pyspark import *
import datetime

# set Spark Context
# ----------------------------
conf = SparkConf().setAppName("miniProject").setMaster("local[*]")
sc = pyspark.SparkContext

# set Spark Session
# ----------------------------
spark = SparkSession \
    .builder \
    .getOrCreate()

# Read in the file
link = "C:\\Users\\linki\\Spark\\spark-3.1.2-bin-hadoop3.2\\spark-3.1.2-bin-hadoop3.2\\pnaptest2.txt"

file_1 = spark.read.text(link).rdd  # Convert file to RDD
mapped = file_1.map(lambda x: x).map(len).cache()  # iterate each line of the file and cache

# calculate how long it takes to read each line
for iter in range(1, 10):
    startTime = datetime.datetime.now()
    seconds = startTime.timestamp()
    for i in mapped.toLocalIterator():
        durationMs = datetime.timedelta(datetime.datetime.now().timestamp() - seconds).total_seconds()
    print("Iteration " + str(iter) + " took " + str(durationMs) + " ms")
