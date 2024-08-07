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


def test_title_has_exclamation():
    # arrange
    df = load_all_csv('movies.csv')

    # act
    result = map_movies(df)

    # assert
    touched_data = result.take(3)
    assert(touched_data[0].name) == 'The Shawshank Redemption!'

def test_any_title_has_exclamation():
    # arrange
    df = load_all_csv('movies.csv')

    # act
    result = map_movies(df)

    # assert
    touched_data = result.take(3)
    assert(touched_data[2].name) == 'The Dark Knight!'

def test_box_office_does_not_change_from_string():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    touched_data = result.take(3)
    assert(touched_data[2].box_office) == '1006234167'

def test_box_office_preserves_estimation_string_flag():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    touched_data = result.take(200)
    assert(touched_data[181].box_office) == '910000 (estimated)'

def test_genre_spreads_into_a_list():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    result.show()
    touched_data = result.take(2)
    # will fail
    assert(touched_data[1].genre) == ['Drama', 'Crime']

def test_rating_does_not_change_from_string():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    touched_data = result.take(2)
    assert(touched_data[1].rating) == "9.2"
