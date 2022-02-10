
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkByExamples.com").getOrCreate()

rdd = spark.sparkContext.parallelize([1,2,3,4,5])
rdd.count()