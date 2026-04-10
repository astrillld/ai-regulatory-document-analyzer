# AI Regulatory Document Analyzer

A modular pipeline for parsing, chunking, indexing, and semantic search over regulatory documents (e.g., AI Act, compliance texts).

## Overview

This project processes long PDF documents and enables efficient semantic search over their content. It is designed for analyzing regulatory texts and extracting meaningful information such as requirements.

## Features

- PDF parsing using PyMuPDF
- Text chunking with configurable overlap
- Semantic embeddings using SentenceTransformers
- Fast similarity search with FAISS
- Requirement detection via rule-based NLP
- Modular and testable architecture

## Pipeline

1. Parse PDF → extract text per page
2. Split text into overlapping chunks
3. Generate embeddings for each chunk
4. Build FAISS index
5. Perform semantic search
6. Detect requirement-like statements

## Example

```bash
python -m src.cli --pdf data/raw/sample.pdf --query "risk management requirements"
