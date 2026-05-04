import math
from collections import defaultdict
from typing import Dict, List

class Indexer:
    
    def __init__(self) -> None:
        self.inverted_index: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.total_docs: int = 0
        self.doc_lengths: Dict[str, int] = {}
        self.tf_idf_matrix: Dict[str, Dict[str, float]] = defaultdict(dict)
        self.idf_cache: Dict[str, float] = {}

    def build_index(self, clean_documents: Dict[str, List[str]]) -> None:
        self.total_docs = len(clean_documents)
        
        if self.total_docs == 0:
            return

        for doc_id, tokens in clean_documents.items():
            self.doc_lengths[doc_id] = len(tokens)
            
            for word in tokens:
                self.inverted_index[word][doc_id] += 1

    def compute_tf_idf(self) -> Dict[str, Dict[str, float]]:
        if self.total_docs == 0:
            return self.tf_idf_matrix
            
        for word, doc_freqs in self.inverted_index.items():
            df = len(doc_freqs)
            idf = math.log10(self.total_docs / float(df))
            self.idf_cache[word] = idf
            
            for doc_id, frequency in doc_freqs.items():
                doc_len = float(self.doc_lengths[doc_id])
                
                if doc_len > 0:
                    tf = frequency / doc_len
                else:
                    tf = 0
                
                self.tf_idf_matrix[doc_id][word] = tf * idf
                
        return self.tf_idf_matrix
