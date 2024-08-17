from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("StateStore-Example") \
        .master("local[3]") \
        .config("spark.sql.shuffle.partitions", 2) \
        .getOrCreate()

spark \
    .read \
    .format("statestore") \
    .load("check-directory") \
    .show(truncate=False)
