from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SimpleSparkApp").getOrCreate()

data = [
    (1, "John", 25),
    (2, "Jane", 30),
    (3, "Bob", 35),
    (4, "Alice", 40)
]

columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)

print("Original DataFrame:")
df.show()

filtered_df = df.filter(col("age") > 30)

print("Filtered DataFrame:")
filtered_df.show()

spark.stop()