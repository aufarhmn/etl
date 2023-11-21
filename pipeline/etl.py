import findspark
from pyspark.sql import SparkSession

from pipeline.extract import Extract
from pipeline.transform import Transform
from pipeline.load import Load

findspark.init()

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

def StartPipeline():
    spark = SparkInit()
    
    YG_df, trend_df = Extract(spark)
    joined_df = Transform(YG_df, trend_df)
    Load(joined_df.toPandas())
    
    spark.stop()
