import os
import pandas as pd

from pyspark.sql import SparkSession
from src.load_movies import map_movies

cwd = os.getcwd()
spark = SparkSession.builder.getOrCreate()

# proof of concept goals
#  * show testing transform logic separate from E/L
#  * generative testing, fake data, etc
#  * roadmap for Phreesia work

def load_all_csv(filename: str) -> pd.DataFrame:
    return spark.read \
        .option('header', True) \
        .option('escape', '"') \
        .csv(os.path.join(cwd, 'tests', 'data', filename))

def test_load_movies():
    df = load_all_csv('movies.csv')
    result = map_movies(df)

    result.show()
    set = result.take(2)

    assert(set[0].name) == 'The Shawshank Redemption!'
    assert(set[1].genre) == ['Drama', 'Crime']