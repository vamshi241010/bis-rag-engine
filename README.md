# 🏗️ BIS Standards Recommendation Engine

## 📌 Overview

An AI-powered system that recommends relevant BIS standards based on product descriptions using hybrid retrieval.

## 🚀 Features

* Hybrid search (FAISS + BM25)
* Fast inference (~0.2–1 sec)
* Clean and explainable output
* Streamlit UI demo

## 🧠 Architecture

User Query → Hybrid Retrieval → Filtering → Output

## 🔍 Retrieval Strategy

* FAISS: semantic similarity
* BM25: keyword matching
* Combined hybrid approach improves accuracy

## 📊 Performance

* Low latency (<1 sec)
* High relevance for construction queries

## ▶️ Run Instructions

### Install dependencies

pip install -r requirements.txt

### Run inference

python inference.py --input sample.json --output out.json

### Run UI

python -m streamlit run app.py

## 🌍 Impact

Helps manufacturers quickly identify BIS standards and improve compliance.


Note: The FAISS index is precomputed. The original dataset PDF is not included to reduce repository size.