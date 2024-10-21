import marimo

__generated_with = "0.8.19"
app = marimo.App(width="medium")


@app.cell
def __(__file__):
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from data_ingestion.data_ingestor_factory import DataIngestorFactory
    return DataIngestorFactory, os, sys


@app.cell
def __(DataIngestorFactory):
    file_path = "data/oil-spill.zip"
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_path)
    df = data_ingestor.ingest(file_path)
    df
    return data_ingestor, df, file_path


if __name__ == "__main__":
    app.run()
