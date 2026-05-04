import os
import sys

# Windows Environment Workarounds for NLTK
from unittest.mock import MagicMock
sys.modules['sklearn'] = MagicMock()

import Core
sys.modules['core'] = Core
from Core import data_loader
sys.modules['Load'] = data_loader

from core.data_loader import DataLoader
from core.text_processor import TextProcessor
from core.indexer import Indexer
from core.search_engine import SearchEngine
import nltk

try:
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)

# Hotfix for SearchEngine raw string mismatch
def _patched_vectorize_query(self, query_text):
    res = self.processor.preprocessing_steps(query_text)
    if not res or 'stemming' not in res:
        return {}
    clean_query_tokens = res['stemming']
    query_vector = {}
    if not clean_query_tokens:
        return query_vector
    token_counts = {}
    for word in clean_query_tokens:
        token_counts[word] = token_counts.get(word, 0) + 1
    vector_length = float(len(clean_query_tokens))
    for word, count in token_counts.items():
        if word in self.indexer.idf_cache:
            tf = count / vector_length
            idf = self.indexer.idf_cache[word]
            query_vector[word] = tf * idf
    return query_vector

SearchEngine._vectorize_query = _patched_vectorize_query

def main():
    loader = DataLoader()
    processor = TextProcessor()
    indexer = Indexer()
    
    target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data')
    if not os.path.exists(target_dir):
        print("Data directory not found. Please ensure it exists.")
        return
        
    docs_cache = loader.load_documents(target_dir)
    
    if not docs_cache:
        print("No documents loaded from Data folder.")
        return
        
    clean_docs = {}
    for d_id, text in docs_cache.items():
        res = processor.preprocessing_steps(text)
        if res and 'stemming' in res:
            clean_docs[d_id] = res['stemming']

    indexer.build_index(clean_docs)
    indexer.compute_tf_idf()
    
    engine = SearchEngine(indexer, processor)
    print(f"Search engine initialized. Loaded {len(docs_cache)} documents.")
    print("Type 'exit', 'quit', or 'q' to stop.")
    
    while True:
        try:
            query = input("\nSearch: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
            
        if not query:
            continue
            
        if query.lower() in ('exit', 'q', 'quit'):
            break
            
        results = engine.search(query, top_k=5)
        
        print(f"\nFound {len(results)} matching results:\n" + "="*50)
        for d_id, score in results:
            # Extract a clean snippet from the original document
            snippet = docs_cache.get(d_id, "").replace('\n', ' ')
            if len(snippet) > 120:
                snippet = snippet[:120] + "..."
                
            print(f" 📄 Document: {d_id}.txt")
            print(f" 🎯 Relevance Score: {score*100:.1f}%")
            print(f" 📝 Excerpt: \"{snippet}\"")
            print("-" * 50)

if __name__ == "__main__":
    main()
