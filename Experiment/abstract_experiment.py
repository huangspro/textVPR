"""
Experiment is a class which load database, queries and search engine to implement a complete experiment
1. load resources
2. do experiment
3. process results(save in files, create graphs and so on)
"""

from abc import ABC, abstractmethod
from SearchEngine.abstract_engine import *

class AbstractExperiment(ABC):
    def __init__(self):
        pass

    # do experiment
    @abstractmethod
    def implement(self):
        pass


    # output experiment results, and save
    @abstractmethod
    def get_experiment_result(self):
        pass