from abc import ABC, abstractmethod
import pandas as pd 


class DataIngestor(ABC):
    @abstractmethod 
    def ingest(self, path:str) -> pd.DataFrame:
        """ Ingest data from a given path """
        pass
        