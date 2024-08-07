from pyspark.sql.functions import lit, concat_ws, split

def map_movies(df):
    map_name = concat_ws('', df.name, lit('!'))
    map_genre = split(df.genre, ',')

    return df.select('name', 'rating', 'genre') \
        .withColumn('name', map_name) \
        .withColumn('genre', map_genre)