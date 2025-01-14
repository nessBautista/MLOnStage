import pytest
import pandas as pd
import os
import zipfile
from data_ingestion.zip_data_ingestor_impl import ZipDataIngestor

@pytest.fixture(scope="function")
def zip_ingestor():
    return ZipDataIngestor()

@pytest.fixture(scope="function")
def test_zip_file():
    test_zip_path = "test_data.zip"
    test_csv_content = "col1,col2\n1,2\n3,4"
    with open("test.csv", "w") as f:
        f.write(test_csv_content)
    with zipfile.ZipFile(test_zip_path, 'w') as zipf:
        zipf.write("test.csv")
    
    yield test_zip_path
    
    # Cleanup
    os.remove(test_zip_path)
    os.remove("test.csv")
    if os.path.exists("extracted_data"):
        for file in os.listdir("extracted_data"):
            os.remove(os.path.join("extracted_data", file))
        os.rmdir("extracted_data")

def test_valid_ingestion(zip_ingestor, test_zip_file):
    """ Test valid ingestion of a zip file containing a CSV """
    df = zip_ingestor.ingest(test_zip_file)
    expected_df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
    pd.testing.assert_frame_equal(df, expected_df)

def test_invalid_file_format(zip_ingestor):
    """ Test ingestion with an invalid file format """
    with pytest.raises(ValueError) as exc_info:
        zip_ingestor.ingest("invalid_file.txt")
    assert str(exc_info.value) == "Invalid file format. Please provide a zip file."

def test_no_csv_in_zip(zip_ingestor, test_zip_file):
    """ Test ingestion when no CSV files are present in the zip """
    with zipfile.ZipFile(test_zip_file, 'w') as zipf:
        zipf.writestr("test.txt", "This is a test file.")
    with pytest.raises(ValueError) as exc_info:
        zip_ingestor.ingest(test_zip_file)
    assert str(exc_info.value) == "No CSV files found in the zip archive."

def test_multiple_csv_in_zip(zip_ingestor, test_zip_file):
    """ Test ingestion when multiple CSV files are present in the zip """
    test_csv_content = "col1,col2\n1,2\n3,4"
    csv_files = ["test1.csv", "test2.csv"]
    
    # Create temporary CSV files
    for file in csv_files:
        with open(file, "w") as f:
            f.write(test_csv_content)
    
    # Add CSV files to the zip
    with zipfile.ZipFile(test_zip_file, 'w') as zipf:
        for file in csv_files:
            zipf.write(file, file)  # Second argument ensures only filename is used in zip
    
    # Run the test
    with pytest.raises(ValueError) as exc_info:
        zip_ingestor.ingest(test_zip_file)
    assert str(exc_info.value) == "Multiple CSV files found in the zip archive. Please specify which file to use."
    
    # Clean up temporary CSV files
    for file in csv_files:
        os.remove(file)