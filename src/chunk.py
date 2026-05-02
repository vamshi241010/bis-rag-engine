import re
import json

def extract_standards(text):
    pattern = r"(IS\s\d+.*?)(?=IS\s\d+|$)"

    matches = re.findall(pattern, text, re.DOTALL)

    chunks = []

    for m in matches:
        id_match = re.search(r"IS\s\d+", m)

        if id_match:
            standard_id = id_match.group()
        else:
            standard_id = "UNKNOWN"

        chunks.append({
            "standard_id": standard_id,
            "text": m.strip()
        })

    return chunks


if __name__ == "__main__":
    with open("data/raw.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = extract_standards(text)

    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    print(f"✅ Extracted {len(chunks)} standards")