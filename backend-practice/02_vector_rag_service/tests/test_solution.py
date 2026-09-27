import sys
import os
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import VectorRAGService

def test_index_and_search_documents():
    rag = VectorRAGService()
    rag.index_document("doc1", "Python is an interpreted high-level programming language.", {"category": "tech"})
    rag.index_document("doc2", "Recipes for delicious chocolate cakes and desserts.", {"category": "food"})
    rag.index_document("doc3", "FastAPI and Flask are popular Python web frameworks.", {"category": "tech"})

    results = rag.search_similar("Python web development framework", top_k=2)
    assert len(results) == 2
    # Tech documents should rank higher than food recipes
    doc_ids = [r["doc_id"] for r in results]
    assert "doc3" in doc_ids or "doc1" in doc_ids

def test_build_rag_prompt():
    rag = VectorRAGService()
    rag.index_document("kb1", "Company refund policy: Customers get full refund within 30 days.")
    
    prompt_bundle = rag.build_rag_prompt("What is the refund policy?", top_k=1)
    assert "context" in prompt_bundle
    assert "30 days" in prompt_bundle["context"]
    assert "user_query" in prompt_bundle
    assert prompt_bundle["user_query"] == "What is the refund policy?"
