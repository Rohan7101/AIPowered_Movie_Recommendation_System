from src.langchain_retriever import search_movies


def test_horror():
    movies = search_movies("I want a scary horror movie")

    assert len(movies) > 0
    assert all(movie.metadata["genre"] == "Horror" for movie in movies)


def test_romance():
    movies = search_movies("I like romantic love stories")

    assert len(movies) > 0
    assert all(movie.metadata["genre"] == "Romance" for movie in movies)


def test_space():
    movies = search_movies("I want a movie about space exploration")
    titles = [movie.metadata["title"] for movie in movies]

    assert "Interstellar" in titles
    assert "Avatar" in titles
