from data_ingestion.data_ingestor_factory import DataIngestorFactory


if __name__ == "__main__":
    file_path = "data/oil-spill.zip"
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_path)
    df = data_ingestor.ingest(file_path)
    print(df.head())
