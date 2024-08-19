import os

from pyspark.sql import SparkSession, DataFrame

cwd = os.getcwd()
spark = SparkSession.builder.getOrCreate()

def load_all_csv(filename: str) -> DataFrame:
    return spark.read \
        .option('header', True) \
        .option('escape', '"') \
        .csv(os.path.join(cwd, 'tests', 'data', filename))