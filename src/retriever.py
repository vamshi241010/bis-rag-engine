import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# load FAISS
index = faiss.read_index("index/faiss.index")

# load metadata
with open("index/meta.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]

# BM25 setup
tokenized_corpus = [t.lower().split() for t in texts]
bm25 = BM25Okapi(tokenized_corpus)


def clean_id(x):
    return x.replace("\n", " ").strip()


def hybrid_search(query, top_k=10):
    # ---------- FAISS ----------
    q_vec = model.encode([query]).astype("float32")
    _, faiss_idx = index.search(q_vec, top_k)

    # ---------- BM25 ----------
    tokenized_query = query.lower().split()
    bm25_scores = bm25.get_scores(tokenized_query)

    bm25_idx = np.argsort(bm25_scores)[::-1][:top_k]

    # ---------- MERGE ----------
    combined_idx = list(faiss_idx[0]) + list(bm25_idx)

    seen = set()
    results = []

    for i in combined_idx:
        item = data[i]
        std_id = clean_id(item["standard_id"])

        if std_id not in seen:
            seen.add(std_id)
            results.append({
                "standard_id": std_id,
                "text": item["text"]
            })

    return results[:top_k]


# test
if __name__ == "__main__":
    q = "cement for road construction"
    res = hybrid_search(q)

    for r in res:
        print("\n---")
        print("Standard:", r["standard_id"])
        print("Text:", r["text"][:150])