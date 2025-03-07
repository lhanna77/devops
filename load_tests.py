import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder.appName("MySparkApp").getOrCreate()
    yield spark
    spark.stop()
    
def test_row_count(spark):
    df = spark.read.parquet("data_lake/dimcurrency")
    assert df.count() > 10000000000, "Table should have at least one row."

# def test_null_values(spark):
#     df = spark.read.parquet("path/to/loaded/table")
#     assert df.filter(col("column_name").isNull()).count() == 0, "Column 'column_name' should not have null values."

# def test_data_range(spark):
#     df = spark.read.parquet("path/to/loaded/table")
#     assert df.agg({"numeric_column": "min"}).collect()[0][0] >= 0, "Numeric column should have values greater than or equal to 0."

# def test_data_uniqueness(spark):
#     df = spark.read.parquet("path/to/loaded/table")
#     assert df.groupBy("unique_id").count().filter(col("count") > 1).count() == 0, "Unique ID should be unique."

# def test_data_consistency(spark):
#     df = spark.read.parquet("path/to/loaded/table")
#     # Example: Check if a calculated column matches a known value
#     calculated_df = df.withColumn("calculated_value", col("column1") * 2)
#     assert calculated_df.filter(col("calculated_value") != col("expected_value")).count() == 0, "Calculated column does not match expected value."

# def test_data_type(spark):
#     df = spark.read.parquet("path/to/loaded/table")
#     assert df.schema["date_column"].dataType.typeName() == "date", "Date column should be of type date."

if __name__ == "__main__":
    pytest.main()