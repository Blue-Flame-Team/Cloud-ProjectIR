import math
from typing import Dict, List, Tuple

from core.indexer import Indexer
from core.text_processor import TextProcessor

class SearchEngine:

    def __init__(self, indexer: Indexer, text_processor: TextProcessor) -> None:
        self.indexer = indexer
        self.processor = text_processor
        
    def _vectorize_query(self, query_text: str) -> Dict[str, float]:
        clean_query_tokens = self.processor.clean_text(query_text)
        query_vector: Dict[str, float] = {}
        
        if not clean_query_tokens:
             return query_vector
             
        token_counts: Dict[str, int] = {}
        for word in clean_query_tokens:
            if word in token_counts:
                token_counts[word] += 1
            else:
                token_counts[word] = 1
            
        vector_length = float(len(clean_query_tokens))
        
        for word, count in token_counts.items():
            if word in self.indexer.idf_cache:
                tf = count / vector_length
                idf = self.indexer.idf_cache[word]
                query_vector[word] = tf * idf
                
        return query_vector

    def _cosine_similarity(self, query_vec: Dict[str, float], doc_vec: Dict[str, float]) -> float:
        dot_product = 0.0
        for word in query_vec:
            if word in doc_vec:
                dot_product += query_vec[word] * doc_vec[word]
        
        query_norm = math.sqrt(sum(val**2 for val in query_vec.values()))
        doc_norm = math.sqrt(sum(val**2 for val in doc_vec.values()))
        
        if query_norm == 0.0 or doc_norm == 0.0:
            return 0.0
            
        return dot_product / (query_norm * doc_norm)
        
    def search(self, query_text: str, top_k: int = 10) -> List[Tuple[str, float]]:
        query_vec = self._vectorize_query(query_text)
        
        if not query_vec:
             return []
             
        scores = []
        for doc_id, doc_vec in self.indexer.tf_idf_matrix.items():
            sim = self._cosine_similarity(query_vec, doc_vec)
            if sim > 0:
                scores.append((doc_id, sim))
                
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
