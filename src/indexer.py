import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load chunks
with open("data/chunks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]

print("🔄 Creating embeddings...")

# Convert text → vectors
embeddings = model.encode(texts, show_progress_bar=True)

# Convert to numpy
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

# Save index
faiss.write_index(index, "index/faiss.index")

# Save metadata (important!)
with open("index/meta.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ FAISS index created successfully")