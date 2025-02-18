from pyspark.sql import SparkSession

# Enable Hive support and specify warehouse directory
spark = SparkSession.builder \
    .appName("DataLoad") \
    .config("spark.sql.catalogImplementation", "hive") \
    .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

# Create database if not exists
spark.sql("CREATE DATABASE IF NOT EXISTS default")

# Verify where tables are stored
warehouse_location = spark.conf.get("spark.sql.warehouse.dir")
print(f"Warehouse location: {warehouse_location}")

# Load data
df = spark.read.format("csv").load('data/DimDate_20250201.txt', header=False, inferSchema=True, delimiter='\t')
df.write.mode("overwrite").saveAsTable("default.my_table")        

# Show tables
spark.sql("SELECT * FROM default.my_table LIMIT 10").show()

# docker-compose up -d

# docker build -t spark-job .
# docker run --network=host spark-job

# docker exec -it spark-master spark-sql
# SELECT * FROM default.my_table LIMIT 10;

