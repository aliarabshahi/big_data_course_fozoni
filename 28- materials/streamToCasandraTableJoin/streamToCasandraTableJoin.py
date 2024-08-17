from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType
from lib.logger import Log4j

from cassandra.cluster import Cluster


def write_to_cassandra(target_df, batch_id):
    cluster = Cluster(['localhost'])
    session = cluster.connect('spark_db')
    target_df.write \
        .format("org.apache.spark.sql.cassandra") \
        .option("keyspace", "spark_db") \
        .option("table", "users") \
        .mode("append") \
        .save()
    target_df.show()


if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[3]") \
        .appName("Stream Table Join Demo") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.sql.shuffle.partitions", 2) \
        .config("spark.cassandra.connection.host", "localhost") \
        .config("spark.cassandra.connection.port", "9042") \
        .getOrCreate()

    logger = Log4j(spark)

    login_schema = StructType([
        StructField("login_id", StringType()),
        StructField("created_time", StringType())
    ])

    kafka_source_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "logins") \
        .option("startingOffsets", "earliest") \
        .load()

    value_df = kafka_source_df.select(from_json(col("value").cast("string"), login_schema).alias("value"))

    login_df = value_df.select("value.*") \
        .withColumn("created_time", to_timestamp(col("created_time"), "yyyy-MM-dd HH:mm:ss"))

    # Here we just read our database for join operation
    user_df = spark.read \
        .format("org.apache.spark.sql.cassandra") \
        .option("keyspace", "spark_db") \
        .option("table", "users") \
        .load()

    join_expr = login_df.login_id == user_df.login_id
    join_type = "inner"

    joined_df = login_df.join(user_df, join_expr, join_type) \
        .drop(login_df.login_id)

    output_df = joined_df.select(col("login_id"), col("user_name"),
                                 col("created_time").alias("last_login"))

    output_query = output_df.writeStream \
        .foreachBatch(write_to_cassandra) \
        .outputMode("update") \
        .option("checkpointLocation", "check-directory") \
        .trigger(processingTime="1 minute") \
        .start()

    logger.info("Waiting-for-Query")
    output_query.awaitTermination()
