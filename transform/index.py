import datetime as dt

import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_utc_timestamp, date_format

def SparkInit():
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
        return spark
    return spark

def Extract(spark) -> tuple:
    YGStock_path = "../frames/2023-11-20_YGStock.csv"
    trend_path = "../frames/2023-11-20_search-trend.csv"

    YG_df = spark.read.csv(YGStock_path, header=True)
    trend_df = spark.read.csv(trend_path, header=True)
    return YG_df, trend_df

def Transform(YG_df, trend_df):
    # Remove columns 'Volume', 'Dividends', 'Stock Splits'
    columns_to_remove = ['Volume', 'Dividends', 'Stock Splits']
    YG_df = YG_df.drop(*columns_to_remove)
    YG_df = YG_df \
                .withColumn("Date", from_utc_timestamp(col("Date"), "Asia/Jakarta")) \
                .withColumn("Date", date_format(col("Date"), "yyyy-MM-dd"))
    trend_df = trend_df \
                    .withColumn("date", from_utc_timestamp(col("date"), "Asia/Jakarta")) \
                    .withColumn("date", date_format(col("date"), "yyyy-MM-dd")) \
                    .withColumnRenamed("Blackpink", "Frequency") \
                    .withColumnRenamed("date", "Date")

    joined = YG_df.join(trend_df, on="Date")
    print(f"joined rows: {joined.count()}")
    joined.show()

    output = f"./out/{dt.datetime.now().strftime('%Y-%m-%d_join')}.csv"

    joined.write.csv(output, header=True, mode="overwrite")
    # YG_df.write.option("header", "true").csv(output)
    # trend_df.write.option("header", "true").csv(output)

if __name__ == '__main__':
    spark = SparkInit()
    YG_df, trend_df = Extract(spark)
    Transform(YG_df, trend_df)
    
    # TODO: Create method to handle load data
    
    spark.stop()