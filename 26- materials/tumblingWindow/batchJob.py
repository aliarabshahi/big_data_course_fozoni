from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import from_json, col, to_timestamp, window, expr, sum
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from lib.logger import Log4j

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Our-Batch-Job") \
        .master("local[*]") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.sql.shuffle.partitions", 2) \
        .getOrCreate()

    logger = Log4j(spark)

    stock_schema = StructType([
        StructField("CreatedTime", StringType()),
        StructField("Type", StringType()),
        StructField("Amount", IntegerType()),
        StructField("BrokerCode", StringType())
    ])

    kafka_df = spark.read \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "trades") \
        .option("startingOffsets", "earliest") \
        .load()

    value_df = kafka_df.select(from_json(col("value").cast("string"), stock_schema).alias("value"))

    trade_df = value_df.select("value.*") \
        .withColumn("CreatedTime", to_timestamp(col("CreatedTime"), "yyyy-MM-dd HH:mm:ss")) \
        .withColumn("Buy", expr("case when Type == 'BUY' then Amount else 0 end")) \
        .withColumn("Sell", expr("case when Type == 'SELL' then Amount else 0 end"))

    window_agg_df = trade_df \
        .groupBy(window(col("CreatedTime"), "15 minute")) \
        .agg(sum("Buy").alias("TotalBuy"),
             sum("Sell").alias("TotalSell"))

    output_df = window_agg_df.select("window.start", "window.end", "TotalBuy", "TotalSell")

    running_total_window = Window.orderBy("end") \
        .rowsBetween(Window.unboundedPreceding, Window.currentRow)

    # running_total_window = Window.orderBy("end") \
    #     .rowsBetween(date_sub("end", 15, "minutes"), Window.currentRow)

    final_output_df = output_df \
        .withColumn("RunningTotalBuy", sum("TotalBuy").over(running_total_window)) \
        .withColumn("RunningTotalSell", sum("TotalSell").over(running_total_window)) \
        .withColumn("NetValue", expr("RunningTotalBuy - RunningTotalSell"))

    final_output_df.show(truncate=False)