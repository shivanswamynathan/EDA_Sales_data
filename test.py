import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app import gender_distribution, relationship

# Load dataset
df = pd.read_csv('sales.csv')

class TestVisualization(unittest.TestCase):

    def test_column_names(self):
        """Check if required columns exist in the DataFrame."""
        required_columns = {'Customer_Gender', 'Age_Group', 'Revenue'}
        self.assertTrue(required_columns.issubset(df.columns), "Missing required columns in the dataset.")

    def test_column_data_types(self):
        """Check if the data types of the columns are correct."""
        self.assertTrue(pd.api.types.is_string_dtype(df['Customer_Gender']), 
                        "Customer_Gender must contain string values.")
        self.assertTrue(pd.api.types.is_string_dtype(df['Age_Group']), 
                        "Age_Group must contain string values.")
        self.assertTrue(pd.api.types.is_numeric_dtype(df['Revenue']), 
                        "Revenue must contain numeric values.")

    def test_non_empty_dataset(self):
        """Ensure the DataFrame is not empty."""
        self.assertFalse(df.empty, "The dataset is empty.")

    def test_row_count(self):
        """Check if the dataset has a reasonable number of rows."""
        self.assertGreater(len(df), 0, "Dataset has zero rows.")
        self.assertLess(len(df), 1_000_000, "Dataset exceeds a reasonable number of rows.")

    def test_no_null_values(self):
        """Check for null values in the dataset."""
        self.assertFalse(df.isnull().values.any(), "Dataset contains null values.")

    def test_gender_plot(self):
        """Ensure gender() method runs without errors."""
        try:
            obj6 = gender_distribution()
            obj6.gender()  # Call the method to ensure it executes without issues.
        except Exception as e:
            self.fail(f"gender() method raised an error: {e}")

    def test_bar_plot(self):
        """Ensure bar() method runs without errors."""
        try:
            obj7 = relationship()
            obj7.bar()  # Call the method to ensure it executes without issues.
        except Exception as e:
            self.fail(f"bar() method raised an error: {e}")

if __name__ == "__main__":
    unittest.main()

