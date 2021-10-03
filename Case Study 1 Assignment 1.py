# 1.Test the spark environment by executing the spark’s HdfsTest.scala example.

import org.apache.spark.sql.SparkSession

import java.util.concurrent.TimeUnit

object HDFSTestcls {
  def main(args: Array[String]): Unit = {
    if (args.length < 1) {
      System.err.println("Usage: HdfsTest <file>")
      System.exit(1)
    }
    val spark = SparkSession
      .builder
      .appName("HdfsTest")
      .getOrCreate()
    val file = spark.read.text(args(0)).rdd
    val mapped = file.map(s => s.length).cache()
    for (iter <- 1 to 10) {
      val startTimeNs = System.nanoTime()
      for (x <- mapped) {
        x + 2
      }
      val durationMs = TimeUnit.NANOSECONDS.toMillis(System.nanoTime() - startTimeNs)
      println(s"Iteration $iter took $durationMs ms")
    }
    println(s"File contents: ${file.map(_.toString).take(1).mkString(",").slice(0, 10)}")
    spark.stop()
  }
}


HDFSTestcls.main(Array("/user/linkinbarb10edu/sqoop_sql2"))

# 2.Try to implement the same example in pyspark and perform spark-submit.

spark-submit HDFSPySpark.py

import datetime
import re
from pyspark.sql import Row

# set Spark Context
# ----------------------------
if __name__ == "__main__":
    conf = SparkConf().setAppName("miniProject").setMaster("local[*]")
    sc = pyspark.SparkContext

    # set Spark Session
    # ----------------------------
    spark = SparkSession \
        .builder \
        .config("spark.logConf", "true") \
        .getOrCreate()

    # Read in the file

     #link = "/mnt/c/users/linki/Spark/spark-3.1.2-bin-hadoop3.2/spark-3.1.2-bin-hadoop3.2/pnaptest2.txt"

    #link = "C:\\Users\\linki\\Spark\\spark-3.1.2-bin-hadoop3.2\\spark-3.1.2-bin-hadoop3.2\\pnaptest2.txt"

    link = "pnaptest.txt"

    file_1 = spark.read.text(link).rdd  # Convert file to RDD
    mapped = file_1.map(lambda x: x).map(len).cache()  # iterate each line of the file and cache - \
    # what is the benefit of the cache in this situation

    # calculate how long it takes to read each line
    for iter in range(1, 11):
        startTime = datetime.datetime.now()
        seconds = startTime.timestamp()
        for i in mapped.toLocalIterator():
            durationMs = int(datetime.timedelta(datetime.datetime.now().timestamp() - seconds).total_seconds())
        print("Iteration " + str(iter) + " took " + str(durationMs) + " ms")

#3.Analyze the behavior of spark application on Spark web UI
# See print screen also provided

# 4.Edit the application and add custom logs. Once executed check the Spark logs.
# See print screen also provided

# 5.Transfer the sample dataset from RDBMS to HDFS
sqoop export --verbose --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/linkinbarb10edu --driver 'com
.mysql.jdbc.Driver' --username linkinbarb10edu --password MaroonEagle68@ --table FINAL_DF3 --m 1 --export-dir '/user/linkinbarb10edu/FINAL_FROM_DF2.csv'

# 6.Validate the loaded data by comparing the statistics of data both in source and HDFS
sqoop eval --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/linkinbarb10edu --driver 'com.mysql.jdbc.Driver' --username linkinbarb10edu --password MaroonEagle68
@ --query 'SELECT COUNT(*) FROM FINAL_DF3'; #OUTPUTS 846404 which compared  to the HDFS count is correct. I also checked the statistical logs provided by the HDFS run and the Import run.

# 7.Create a new directory EQ in HDFS and transfer the data where series is EQ
hdfs dfs -mkdir /user/linkinbarb10edu/EQ

# 8.Set total trades which are less than 500 to 0 and transfer only updated rows.
#8a: Update the table in MYSQL
UPDATE FINAL_DF3 SET TOTALTRADES = 0 WHERE TOTALTRADES <= 500;

#8b: Transfer the updated table to HDFS
sqoop import --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.inte
rnal/linkinbarb10edu --driver 'com.mysql.jdbc.Driver' --username linkinbarb10edu --password MaroonEagle68@ -
-query 'SELECT * FROM FINAL_DF3 WHERE $CONDITIONS AND TOTALTRADES = 0' --m 1 --target-dir '/user/linkinbarb1
0edu/EQ_LE500';