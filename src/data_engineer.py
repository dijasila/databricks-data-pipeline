from pyspark.sql import functions as F

def engineer_data(df):
    # Example transformation: adding a new column by manipulating existing columns
    df = df.withColumn("new_column", df["existing_column"] * 10)

    # Filtering rows
    df = df.filter(df["new_column"] > 100)

    # Grouping and aggregating
    grouped_df = df.groupBy("group_column").agg(F.mean("new_column").alias("mean_value"))

    return grouped_df