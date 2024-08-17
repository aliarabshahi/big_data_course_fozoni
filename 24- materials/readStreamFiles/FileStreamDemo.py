from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

from lib.logger import Log4j

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("File-Streaming-Demo") \
        .master("local[3]") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.sql.streaming.schemaInference", "true") \
        .getOrCreate()

    logger = Log4j(spark)

    #🛑read ########################################

    raw_df = spark.readStream \
        .format("json") \
        .option("path", ".\json_input") \
        .option("maxFilesPerTrigger", 1) \
        .load()

    # raw_df.printSchema()

    #🛑transform ########################################

    explode_df = raw_df.selectExpr("InvoiceNumber", "CreatedTime", "StoreID", "PosID",
                                   "CustomerType", "PaymentMethod", "DeliveryType", "DeliveryAddress.City",
                                   "DeliveryAddress.State",
                                   "DeliveryAddress.PinCode", "explode(InvoiceLineItems) as LineItem")

    flattened_df = explode_df \
        .withColumn("ItemCode", expr("LineItem.ItemCode")) \
        .withColumn("ItemDescription", expr("LineItem.ItemDescription")) \
        .withColumn("ItemPrice", expr("LineItem.ItemPrice")) \
        .withColumn("ItemQty", expr("LineItem.ItemQty")) \
        .withColumn("TotalValue", expr("LineItem.TotalValue")) \
        .drop("LineItem")

    #🛑write ########################################

    invoiceWriterQuery = flattened_df.writeStream \
        .format("csv") \
        .queryName("Flattened-Invoice-Writer") \
        .outputMode("append") \
        .option("path", ".\output") \
        .option("checkpointLocation", "check-directory") \
        .trigger(processingTime="1 minute") \
        .start()

    #🛑🛑in .format("json") we can use "csv" or "parquet" extensions🛑🛑

    logger.info("Flattened Invoice Writer started")
    invoiceWriterQuery.awaitTermination()
