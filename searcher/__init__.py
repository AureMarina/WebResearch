import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from enum import Enum
from searchers.faiss_searcher import FaissSearcher

from searchers.base import BaseSearcher
from searchers.faiss_searcher import FaissSearcher, ReasonIrSearcher

class SearcherType(Enum):
    FAISS = ("faiss", FaissSearcher)
    REASONIR = ("reasonir", ReasonIrSearcher)

    def __init__(self, cli_name, searcher_class):
        self.cli_name = cli_name
        self.searcher_class = searcher_class
    
    @classmethod
    def get_choices(cls):
        """返回类的类型"""
        return [search_type.cli_name for search_type in cls]
    
    @classmethod
    def get_search_class(cls, cli_name):
        for g in cls:
            if g.cli_name == cli_name:
                return g.searcher_class
        raise ValueError(f"Unknown search type: {cli_name}")
    

__all__ = [
    "BaseSearcher",
    "SearcherType"
]