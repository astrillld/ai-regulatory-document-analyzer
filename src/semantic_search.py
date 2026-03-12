from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

chunks = [
    "first_metrics",
    "second_metrics",
    "third_metrics"
]

chunk_embeddings = model.encode(chunks)
chunk_embeddings = np.array(chunk_embeddings).astype("float32")

index = faiss.IndexFlatL2(chunk_embeddings.shape[1])
index.add(chunk_embeddings)

query = "good project"  

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

distances, indices = index.search(query_embedding, k=2)

for i in range(len(indices[0])):
    print(f"Chunk {indices[0][i]}: {chunks[indices[0][i]]} (Distance: {distances[0][i]})")
