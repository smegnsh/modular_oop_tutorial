# tests/test_model.py

import unittest
from unittest.mock import patch, MagicMock
from scripts.model import train_model, save_model, load_model  # Correct import

class TestModelFunctions(unittest.TestCase):

    @patch("scripts.model.train_test_split")
    @patch("scripts.model.RandomForestClassifier")
    def test_train_model(self, mock_rf_class, mock_train_test_split):
        # Mock the split
        X_train, X_test = MagicMock(), MagicMock()
        y_train, y_test = MagicMock(), MagicMock()
        mock_train_test_split.return_value = (X_train, X_test, y_train, y_test)

        # Mock the model
        mock_model = MagicMock()
        mock_rf_class.return_value = mock_model

        # Call train_model
        model, X_test_out, y_test_out = train_model(MagicMock(), MagicMock())

        # Assertions
        mock_train_test_split.assert_called_once()
        mock_rf_class.assert_called_once()
        mock_model.fit.assert_called_once_with(X_train, y_train)
        self.assertEqual(model, mock_model)
        self.assertEqual(X_test_out, X_test)
        self.assertEqual(y_test_out, y_test)

    @patch("scripts.model.joblib.dump")
    def test_save_model(self, mock_dump):
        mock_model = MagicMock()
        save_model(mock_model, "fake_path.pkl")
        mock_dump.assert_called_once_with(mock_model, "fake_path.pkl")

    @patch("scripts.model.joblib.load")
    def test_load_model(self, mock_load):
        mock_model = MagicMock()
        mock_load.return_value = mock_model
        result = load_model("fake_path.pkl")
        mock_load.assert_called_once_with("fake_path.pkl")
        self.assertEqual(result, mock_model)

if __name__ == "__main__":
    unittest.main()
