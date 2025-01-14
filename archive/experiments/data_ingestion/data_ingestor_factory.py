from .data_ingestor_interface import DataIngestor
from .zip_data_ingestor_impl import ZipDataIngestor

class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_path: str) -> DataIngestor:
        if file_path.endswith(".zip"):
            return ZipDataIngestor()
        else:
            raise ValueError("Invalid file format. Please provide a zip file.")
