### Install Apache Spark

https://spark.apache.org/

### Download and set winutils

https://github.com/cdarlint/winutils 

### Install PyCharm Community Edition 

https://www.jetbrains.com/pycharm/download/?section=windows 

### Set Some Environments Variables 

- SPARK_HOME= D:\tools\spark3.5.1\bin

- HADOOP_HOME= C:\hadoop-3.3.5\bin

- PYSPARK_PYTHON= C:\Users\Golestan\AppData\Local\Programs\Python\Python311\python
  

  🛑`PYSPARK_PYTHON`🛑 is an environment variable used to specify the Python executable that PySpark (*PySpark is the Python API for Apache Spark*) should use when running Python code.
  

- PYTHONPATH= %SPARK_HOME%\python;%SPARK_HOME%\python\lib\py4j-0.10.9.7-src.zip

### Spark UI

Immediately after creating `SparkSession` we can go to the following URL and see what's happening: 

http://localhost:4040/