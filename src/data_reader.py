from pyspark.sql import SparkSession

def read_data(file_path):
    # Initialize a Spark session
    spark = SparkSession.builder \
        .appName("Databricks Data Pipeline") \
        .getOrCreate()
    
    # Read the CSV file into a DataFrame
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    
    return df