from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("StateStore-Example") \
        .master("local[3]") \
        .config("spark.sql.shuffle.partitions", 2) \
        .getOrCreate()

spark \
    .read \
    .format("state-metadata") \
    .load("check-directory") \
    .show(truncate=False)
