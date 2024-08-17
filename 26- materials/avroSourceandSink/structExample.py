from pyspark.sql import SparkSession
from pyspark.sql.functions import struct

if __name__ == "__main__":
    spark = SparkSession.builder.appName("StructColumnExample").getOrCreate()

    data = [(1, "Alice", 28), (2, "Bob", 35)]

    df = spark.createDataFrame(data, ["id", "name", "age"])

    df_with_struct = df.withColumn("person_info", struct("name", "age"))

    df_with_struct.show()
