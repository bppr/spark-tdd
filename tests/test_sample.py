from tests.support import load_all_csv

from src.load_movies import map_movies

def test_title_has_exclamation():
    # arrange / GIVEN
    df = load_all_csv('movies.csv')

    # act / WHEN
    result = map_movies(df)

    # assert / THEN
    touched_data = result.take(3)
    assert(touched_data[0].name) == 'The Shawshank Redemption!'

def test_any_title_has_exclamation():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    touched_data = result.take(3)
    assert(touched_data[2].name) == 'The Dark Knight', 'The assigned name was incorrect'

def test_box_office_rounds_millions_to_nearest_2_decimals():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    touched_data = result.take(3)
    assert(touched_data[2].box_office) == '1006.23M'

def test_box_office_preserves_estimation_string_flag():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    touched_data = result.take(200)
    assert(touched_data[181].box_office) == '0.91M'

def test_genre_spreads_into_a_list():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    # result.show()
    touched_data = result.take(2)
    # will fail
    assert(touched_data[1].genre) == ['Drama', 'Crime']

def test_rating_does_not_change_from_string():
    df = load_all_csv('movies.csv')

    result = map_movies(df)

    touched_data = result.take(2)
    assert(touched_data[1].rating) == "9.2"
