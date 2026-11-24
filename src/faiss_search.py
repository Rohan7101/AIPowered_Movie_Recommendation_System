import faiss
from sentence_transformers import SentenceTransformer
from dataset import movies

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate movie embeddings
embeddings = model.encode(
    movies["content"].tolist(),
    normalize_embeddings=True
)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)


# Search for similar movies
def recommend_movies(query):
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    scores, indices = index.search(query_embedding, 5)

    results = []

    for i, score in zip(indices[0], scores[0]):
        if score >= 0.40:
            movie = movies.iloc[i]

            results.append({
                "title": movie["title"],
                "genre": movie["genre"],
                "year": int(movie["year"]),
                "description": movie["description"],
                "similarity": round(float(score), 2)
            })

    return results


# Run only when executed directly
if __name__ == "__main__":
    query = input("Enter your movie preference: ")

    for movie in recommend_movies(query):
        print(movie["title"], movie["similarity"])
