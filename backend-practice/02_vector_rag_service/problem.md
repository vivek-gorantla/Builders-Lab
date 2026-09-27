# Problem 02: Semantic Vector Search & RAG Engine

## 1. Scenario
Enterprise AI systems use Retrieval-Augmented Generation (RAG) to inject proprietary knowledge base document chunks into LLM prompts using vector similarity search (cosine similarity).

## 2. Goal
Build `VectorRAGService` to generate vector embeddings (using TF-IDF / term frequency vectorization or embedding function), index document chunks, perform top-$K$ cosine similarity search, and construct RAG prompts.

## 3. Required Class
- `VectorRAGService`

## 4. Required Methods
- `index_document(doc_id: str, text: str, metadata: Optional[dict] = None) -> None`
- `search_similar(query_text: str, top_k: int = 3) -> list[dict]`
- `build_rag_prompt(query_text: str, top_k: int = 3) -> dict`

## 5. Behavior
- `index_document`: Converts document text to a vector embedding (e.g. term frequency vector or embedding calculation), stores vector and metadata.
- `search_similar`: Converts `query_text` to query vector, computes Cosine Similarity ($rac{A \cdot B}{\|A\| \|B\|}$) against all indexed vectors, and returns top `top_k` documents sorted by similarity score descending.
- `build_rag_prompt`: Searches top `top_k` relevant documents, combines text content into a `context` string, and returns `{"system_prompt": "Answer using the context provided.", "context": context_str, "user_query": query_text}`.

## 6. Validation Rules
- Duplicate `doc_id` updates existing indexed document.
- Empty search query raises `ValueError`.

## 7. Edge Cases
- Searching an empty vector index returns empty list.

## 8. Examples
```python
rag = VectorRAGService()
rag.index_document("1", "PostgreSQL is a relational database.")
prompt = rag.build_rag_prompt("Tell me about databases")
```

## 9. Constraints
- Pure Python standard library (e.g. `math`).

## 10. Left for Developer Decision
- Vector representation algorithm (TF-IDF vectorizer, word overlap hash, or custom vector calculator).
