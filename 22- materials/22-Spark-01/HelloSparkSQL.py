from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[1]") \
        .appName("Hello-Spark-SQL") \
        .getOrCreate()

    surveyDF = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("data/sample.csv")

    surveyDF.createOrReplaceTempView("survey_tbl")
    countDF = spark.sql("select Country, count(1) as count from survey_tbl where Age<40 group by Country")

    countDF.show()
