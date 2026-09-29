"""
An AbstractSearchEngine defines an interface of how to search and return results
1. Given a list of images paths, text descriptions
2. then search in the database through some ways
3. At last, return a list of items from database
"""

from Dataset.vpr import *
from abc import ABC, abstractmethod

class AbstractSearchEngine(ABC):
    def __init__(self, database):
        self.database = database

    # Given a list of queries(images tensors, texts and so on), search in the database
    # return a list of items from database
    @abstractmethod
    def search(self, queries:list) -> list:
        pass

