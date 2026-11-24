from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_core.documents import Document
from src.dataset import movies

# Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True}
)

# Convert movie records into LangChain Documents
documents = []

for _, movie in movies.iterrows():
    doc = Document(
        page_content=movie["content"],
        metadata={
            "title": movie["title"],
            "genre": movie["genre"],
            "year": int(movie["year"]),
            "description": movie["description"]
        }
    )
    documents.append(doc)

# Create a FAISS vector store
vector_store = FAISS.from_documents(
    documents,
    embeddings,
    distance_strategy=DistanceStrategy.MAX_INNER_PRODUCT
)

# Search and filter movies

def search_movies(query):
    results = vector_store.similarity_search_with_score(query, k=100)

    matching_movies = []
    query_lower = query.lower()

    genres = {
        "romantic": "Romance",
        "romance": "Romance",
        "horror": "Horror",
        "scary": "Horror",
        "comedy": "Comedy",
        "funny": "Comedy",
        "action": "Action"
    }

    requested_genre = None

    for word, genre in genres.items():
        if word in query_lower:
            requested_genre = genre
            break

    for movie, score in results:
        genre_match = movie.metadata["genre"] == requested_genre

        if score >= 0.39 or (requested_genre and genre_match):
            matching_movies.append(movie)

    return matching_movies[:5]


if __name__ == "__main__":
    queries = [
        "I want a scary horror movie",
        "I like romantic love stories",
        "I want a movie about space exploration",
        "I want an action movie with superheroes",
        "I want a funny comedy movie"
    ]

    for query in queries:
        print("\nPreference:", query)

        results = search_movies(query)

        if results:
            for movie in results:
                print("-", movie.metadata["title"])
        else:
            print("No matching movies found.")

