### See some of our schemas

#### Sample Data for Schema Definition

```json
{"CreatedTime": "2024-02-05 10:05:00", "Type": "BUY", "Amount": 500, "BrokerCode": "ABX"}
```

#### Step One

```python
stock_schema = StructType([
        StructField("CreatedTime", StringType()),
        StructField("Type", StringType()),
        StructField("Amount", IntegerType()),
        StructField("BrokerCode", StringType())
    ])

kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "trades") \
        .option("startingOffsets", "earliest") \
        .load()
    
kafka_df.printSchema()
```

```
root
 |-- key: binary (nullable = true)
 |-- value: binary (nullable = true)
 |-- topic: string (nullable = true)
 |-- partition: integer (nullable = true)
 |-- offset: long (nullable = true)
 |-- timestamp: timestamp (nullable = true)
 |-- timestampType: integer (nullable = true)
```

#### Step Two

```python
value_df = kafka_df.select(from_json(col("value").cast("string"), stock_schema).alias("value"))

value_df.printSchema()
```

```
root
 |-- value: struct (nullable = true)
 |    |-- CreatedTime: string (nullable = true)
 |    |-- Type: string (nullable = true)
 |    |-- Amount: integer (nullable = true)
 |    |-- BrokerCode: string (nullable = true)
```

#### Step Three

```
trade_df = value_df.select("value.*") \
        .withColumn("CreatedTime", to_timestamp(col("CreatedTime"), "yyyy-MM-dd HH:mm:ss")) \
        .withColumn("Buy", expr("case when Type == 'BUY' then Amount else 0 end")) \
        .withColumn("Sell", expr("case when Type == 'SELL' then Amount else 0 end"))

trade_df.printSchema()
```

```
root
 |-- CreatedTime: timestamp (nullable = true)
 |-- Type: string (nullable = true)
 |-- Amount: integer (nullable = true)
 |-- BrokerCode: string (nullable = true)
 |-- Buy: integer (nullable = true)
 |-- Sell: integer (nullable = true)
```

