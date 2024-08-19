from pyspark.sql import DataFrame
from pyspark.sql.functions import *

def map_movies(df) -> DataFrame:
    map_name = concat_ws('', df.name, lit('!'))
    map_genre = split(df.genre, ',')
    map_box_office = concat_ws('', round(try_divide(btrim(df.box_office, lit(' (estimated)')), lit(1_000_000)), 2), lit('M'))
    
    
    return df.select('name', 'rating', 'genre', 'box_office') \
        .withColumn('name', map_name) \
        .withColumn('genre', map_genre) \
        .withColumn('box_office', map_box_office)
        