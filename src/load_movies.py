from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType

@udf()
def map_name(m): return m + '!'

@udf(returnType=ArrayType(StringType()))
def map_genre(m): return m.split(',')

def map_movies(df):
    return df.select('name', 'rating', 'genre') \
        .withColumn('name', map_name(df.name)) \
        .withColumn('genre', map_genre(df.genre))