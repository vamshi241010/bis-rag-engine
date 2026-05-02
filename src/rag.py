from src.retriever import hybrid_search
import re


def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"[^a-zA-Z0-9 :().-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def generate_results(query):
    docs = hybrid_search(query, top_k=4)

    final = []
    query_words = query.lower().split()

    for d in docs:
        std_id = clean_text(d["standard_id"])
        text = clean_text(d["text"])

        # stronger relevance check
        if sum(word in text.lower() for word in query_words) >= 2:
            final.append({
                "standard": std_id,
                "reason": f"Relevant to {query}: {text[:100]}"
            })

        if len(final) == 5:
            break

    # fallback if nothing matched (IMPORTANT)
    if not final:
        for d in docs[:3]:
            final.append({
                "standard": clean_text(d["standard_id"]),
                "reason": clean_text(d["text"])[:100]
            })

    return final