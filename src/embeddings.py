from sentence_transformers import SentenceTransformer
from dataset import movies

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(movies["content"].tolist())

print("Embedding Shape:", embeddings.shape)
