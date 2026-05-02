import json
import time
from src.rag import generate_results

def run(input_path, output_path):
    with open(input_path, "r") as f:
        data = json.load(f)

    output = []

    for item in data:
        start = time.time()

        query = item["query"]
        results = generate_results(query)

        latency = time.time() - start

        output.append({
            "id": item["id"],
            "retrieved_standards": results,
            "latency_seconds": round(latency, 3)
        })

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")

    args = parser.parse_args()

    run(args.input, args.output)