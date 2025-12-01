import unittest
from unittest.mock import patch
import pandas as pd

from scripts.plot_utils import PlotUtils  # Adjust to your file structure


class TestPlotUtils(unittest.TestCase):
    """TDD-style tests for PlotUtils class, mocking plotting functions."""

    def setUp(self):
        """Create a small dummy DataFrame for testing."""
        self.df = pd.DataFrame({
            "age": [25, 35, 45],
            "income": [3000, 4000, 5000],
            "loan_status": [0, 1, 0]
        })
        self.plotter = PlotUtils(self.df)

    # -------------------------------
    # Test Histogram
    # -------------------------------
    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.savefig")
    @patch("seaborn.histplot")
    def test_histogram(self, mock_hist, mock_save, mock_show):
        """histogram() calls seaborn.histplot and matplotlib save/show."""
        self.plotter.histogram("age", bins=5, save_path="plot.png")

        mock_hist.assert_called_once_with(self.df["age"], bins=5, kde=True)
        mock_save.assert_called_once_with("plot.png", bbox_inches='tight')
        mock_show.assert_called_once()

    # -------------------------------
    # Test Scatter Plot
    # -------------------------------
    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.savefig")
    @patch("seaborn.scatterplot")
    def test_scatter(self, mock_scatter, mock_save, mock_show):
        """scatter() calls seaborn.scatterplot correctly."""
        self.plotter.scatter("age", "income", hue="loan_status", save_path="scatter.png")

        mock_scatter.assert_called_once_with(
            data=self.df, x="age", y="income", hue="loan_status"
        )
        mock_save.assert_called_once_with("scatter.png", bbox_inches='tight')
        mock_show.assert_called_once()

    # -------------------------------
    # Test Line Plot
    # -------------------------------
    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.savefig")
    @patch("seaborn.lineplot")
    def test_line(self, mock_line, mock_save, mock_show):
        """line() calls seaborn.lineplot correctly."""
        self.plotter.line("age", "income", save_path="line.png")

        mock_line.assert_called_once_with(data=self.df, x="age", y="income")
        mock_save.assert_called_once_with("line.png", bbox_inches='tight')
        mock_show.assert_called_once()

    # -------------------------------
    # Test Prediction Plot
    # -------------------------------
    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.savefig")
    @patch("seaborn.countplot")
    def test_plot_predictions(self, mock_countplot, mock_save, mock_show):
        """plot_predictions() calls seaborn.countplot correctly."""
        actual = [0, 1, 0]
        predicted = [1, 1, 0]

        self.plotter.plot_predictions(actual, predicted, save_path="pred_plot.png")

        # seaborn.countplot should be called with melted DataFrame
        args = mock_countplot.call_args[1]
        self.assertIn("data", args)
        self.assertIn("x", args)
        self.assertEqual(args["x"], "Loan_Status")
        self.assertEqual(args["hue"], "Type")

        mock_save.assert_called_once_with("pred_plot.png", bbox_inches='tight')
        mock_show.assert_called_once()


if __name__ == "__main__":
    unittest.main()