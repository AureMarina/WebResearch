from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import argparse

class BaseSearcher(ABC):
    
    @classmethod
    @abstractmethod
    def parse_args(cls, parser: argparse.ArgumentParser) -> None:
        pass

    @abstractmethod
    def __init__(self, args):
        """Initialize the searcher with parsed arguments."""
        pass

    @abstractmethod
    def search(self, query: str, k: int = 10):
        """
        Perform search and return results

        Args:
            query: Search query string
            k: Number of results to return
        
        Returns: 
            List of search results with format: 
            [
            {"docid": str, "text": str, "score": float}, ...
            ]
        """
        pass

    def get_document(self, docid: str):
        """
        可选: 按docid取全文, 返回 {}
        """
        return None

    @property
    def search_type(self):
        """Return the type of search (e.g., 'BM25', 'FAISS')"""
        return self.__class__.__name__
    
    