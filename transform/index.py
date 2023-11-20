import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("CSVTransformation") \
    .master("local[*]") \
    .getOrCreate()

try:
    sc = spark.sparkContext
    print("Connected to Spark!")

except Exception as e:
    print("Creating new SparkSession...")
    spark = SparkSession.builder \
        .appName("CSVTransformation") \
        .master("local[*]") \
        .getOrCreate()

input_path = "./YGStock.csv"

df = spark.read.csv(input_path, header=True)

print("Initial DataFrame:")
df.show()

# Remove columns 'Volume', 'Dividends', 'Stock Splits'
columns_to_remove = ['Volume', 'Dividends', 'Stock Splits']
df = df.drop(*columns_to_remove)

# Format the 'Date' column
df = df.withColumn("Date", col("Date").substr(1, 10))

print("Transformed DataFrame:")
df.show()

output_path = "./YGStockTransformed"

df.write.mode("overwrite").option("header", "true").csv(output_path)

spark.stop()