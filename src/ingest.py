import fitz  # PyMuPDF

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


if __name__ == "__main__":
    pdf_path = "data/dataset.pdf"  # YOUR FILE NAME

    text = extract_text(pdf_path)

    with open("data/raw.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("✅ PDF extracted successfully")