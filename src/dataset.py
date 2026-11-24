import pandas as pd

# Read the dataset
movies = pd.read_csv("data/movies.csv")

# Combine movie information
movies["content"] = (
    movies["title"] + " " +
    movies["genre"] + " " +
    movies["description"]
)

if __name__ == "__main__":
    print("Total movies:", len(movies))
    print("Unique IDs:", movies["movie_id"].nunique())
    print("Missing values:", movies.isnull().sum().sum())
    print("\nMovies by genre:")
    print(movies["genre"].value_counts())