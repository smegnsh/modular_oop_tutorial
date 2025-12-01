import matplotlib.pyplot as plt   # Import matplotlib for plotting figures
import seaborn as sns             # Import seaborn for advanced plotting (built on top of matplotlib)
import pandas as pd               # Import pandas for handling data frames

sns.set(style="whitegrid")        # Set the seaborn plotting style to "whitegrid" for all plots


class PlotUtils:
    """
    A utility class for plotting data in the Loan Prediction project.
    Supports histogram, scatter, line plots, and prediction comparison.
    """

    def __init__(self, df):
        self.df = df               # Store the DataFrame to be used in plotting methods

    def histogram(self, column, bins=10, title=None, save_path=None):
        plt.figure(figsize=(8, 5))                                  # Create a new figure of size 8x5 inches
        sns.histplot(self.df[column], bins=bins, kde=True)           # Plot histogram of the specified column with KDE curve
        plt.title(title or f'Histogram of {column}')                # Set the plot title; use default if none provided
        plt.xlabel(column)                                          # Label x-axis with column name
        plt.ylabel('Frequency')                                     # Label y-axis as 'Frequency'
        if save_path:                                               # If a save path is provided
            plt.savefig(save_path, bbox_inches='tight')             # Save the plot to file, trimming extra whitespace
        plt.show()                                                  # Display the plot

    def scatter(self, x_col, y_col, hue=None, title=None, save_path=None):
        plt.figure(figsize=(8, 5))                                  # Create a new figure of size 8x5 inches
        sns.scatterplot(data=self.df, x=x_col, y=y_col, hue=hue)   # Scatter plot with optional hue for coloring
        plt.title(title or f'Scatter plot of {y_col} vs {x_col}')  # Set title; default shows y vs x
        plt.xlabel(x_col)                                           # Label x-axis
        plt.ylabel(y_col)                                           # Label y-axis
        if save_path:                                               # If a file path is provided
            plt.savefig(save_path, bbox_inches='tight')             # Save the plot to file
        plt.show()                                                  # Display the plot

    def line(self, x_col, y_col, title=None, save_path=None):
        plt.figure(figsize=(8, 5))                                  # Create a new figure
        sns.lineplot(data=self.df, x=x_col, y=y_col)               # Line plot of y vs x
        plt.title(title or f'Line plot of {y_col} vs {x_col}')     # Set title
        plt.xlabel(x_col)                                           # Label x-axis
        plt.ylabel(y_col)                                           # Label y-axis
        if save_path:                                               # If a file path is provided
            plt.savefig(save_path, bbox_inches='tight')             # Save the plot
        plt.show()                                                  # Display the plot

    def plot_predictions(self, actual, predicted, title="Actual vs Predicted Loans", save_path=None):
        df_plot = pd.DataFrame({"Actual": actual, "Predicted": predicted})  # Create a DataFrame from actual and predicted values
        plt.figure(figsize=(8, 5))                                        # Create a new figure
        sns.countplot(                                                     # Plot counts of loan status
            data=df_plot.melt(var_name="Type", value_name="Loan_Status"),  # Melt DataFrame to long format for seaborn
            x="Loan_Status",                                               # Set x-axis as Loan_Status
            hue="Type"                                                     # Differentiate counts for Actual vs Predicted
        )
        plt.title(title)                                                   # Set the plot title
        plt.xlabel("Loan Status (0 = Not Approved, 1 = Approved)")        # Label x-axis
        plt.ylabel("Count")                                                # Label y-axis
        if save_path:                                                      # If a file path is provided
            plt.savefig(save_path, bbox_inches='tight')                    # Save the figure to file
        plt.show()                                                         # Display the plot
