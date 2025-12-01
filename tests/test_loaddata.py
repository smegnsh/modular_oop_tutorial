import unittest                     # Import Python's built-in testing framework
from unittest.mock import patch     # patch allows us to replace functions with mocks during tests
import pandas as pd                 # Import pandas to create mock DataFrames
from scripts.data_loader import load_data   # Import the function being tested (replace module name)


class TestLoadData(unittest.TestCase):    # Create a test class inheriting from unittest.TestCase

    @patch("pandas.read_csv")             # Replace pandas.read_csv with a mock during this test
    def test_load_csv(self, mock_read_csv):  # mock_read_csv is the mocked version of read_csv
        mock_df = pd.DataFrame({"a": [1, 2]})  # Create a fake DataFrame to act as test data
        mock_read_csv.return_value = mock_df   # Make read_csv return our fake DataFrame

        result = load_data("data.csv")   # Call the function using a CSV file extension

        mock_read_csv.assert_called_once_with("data.csv")  # Ensure read_csv was called with correct file name
        self.assertTrue(result.equals(mock_df))            # Check that returned DataFrame matches mock_df

    @patch("pandas.read_excel")           # Mock pandas.read_excel
    def test_load_excel(self, mock_read_excel):
        mock_df = pd.DataFrame({"x": [10, 20]})   # Create a fake DataFrame
        mock_read_excel.return_value = mock_df    # Set return value of read_excel

        result = load_data("file.xlsx")           # Call load_data with an Excel file

        mock_read_excel.assert_called_once_with("file.xlsx")  # Verify correct call
        self.assertTrue(result.equals(mock_df))               # Result must match mock_df

    @patch("pandas.read_json")            # Mock pandas.read_json
    def test_load_json(self, mock_read_json):
        mock_df = pd.DataFrame({"key": ["value"]})   # Fake DataFrame for JSON file
        mock_read_json.return_value = mock_df         # Mock return value

        result = load_data("info.json")               # Call load_data with JSON file

        mock_read_json.assert_called_once_with("info.json")  # Ensure correct call
        self.assertTrue(result.equals(mock_df))              # Check returned DF matches

    def test_unsupported_file_type(self):
        # Expecting ValueError for unsupported file types
        with self.assertRaises(ValueError) as context:
            load_data("file.txt")                      # .txt extension is unsupported

        # Ensure error message contains expected text
        self.assertIn("Unsupported file type", str(context.exception))

    @patch("pandas.read_csv", side_effect=Exception("File error"))  
    # Mock read_csv so it always raises an exception
    def test_loading_failure(self, mock_read_csv):
        # Calling load_data should raise ValueError because pandas failed
        with self.assertRaises(ValueError) as context:
            load_data("bad.csv")

        # Validate the error message contains the expected substrings
        self.assertIn("Failed to load file", str(context.exception))
        self.assertIn("bad.csv", str(context.exception))  # File name should appear in error message


if __name__ == "__main__":       # Run tests when the file is executed directly
    unittest.main()
