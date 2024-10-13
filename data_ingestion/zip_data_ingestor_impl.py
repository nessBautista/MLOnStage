from .data_ingestor_interface import DataIngestor
import pandas as pd 
import zipfile 
import os

class ZipDataIngestor(DataIngestor):
    def ingest(self, path:str) -> pd.DataFrame:
        """ Ingest data from a given path """
        if not path.endswith(".zip"):
            raise ValueError("Invalid file format. Please provide a zip file.")
        
        # Extract the zip file 
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")

        # find the csv file in the extracted data 
        extracted_files = os.listdir("extracted_data")
        csv_files = [file for file in extracted_files if file.endswith(".csv")]

        if len(csv_files) == 0:
            raise ValueError("No CSV files found in the zip archive.")
        
        if len(csv_files) > 1:
            raise ValueError("Multiple CSV files found in the zip archive. Please specify which file to use.")
        
        # Read the CSV file 
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)
        return df
        

  
if __name__ == "__main__":
    print("Hello")
    ingestor = ZipDataIngestor()
    # Add some demo code here, e.g.:
    # df = ingestor.ingest("path/to/some/test/data.zip")
    # print(df.head())
