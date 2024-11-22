import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataPreprocessor:
    """Handles preprocessing tasks."""
    
    def __init__(self, dataframe):
        self.df = dataframe

    def visualize_missing_values(self):
        """Visualize missing values in the dataset."""
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.df.isnull(), cmap="viridis", cbar=False, yticklabels=False)
        plt.title("Missing Values Visualization")
        plt.xlabel("Columns")
        plt.ylabel("Rows")
        plt.show()

    def dataset_info(self):
        """Print dataset information."""
        print(self.df.info())


class DataAnalyzer:
    """Handles data analysis tasks."""

    def __init__(self, dataframe):
        self.df = dataframe

    def calculate_summary_statistics(self):
        """Calculate and print summary statistics (mean, median, mode) for numeric columns."""
        numeric_columns = self.df.select_dtypes(include=['number'])
        mean_values = numeric_columns.mean()
        median_values = numeric_columns.median()
        mode_values = numeric_columns.mode().iloc[0]
        print(f"Mean:\n{mean_values}\n")
        print(f"Median:\n{median_values}\n")
        print(f"Mode:\n{mode_values}\n")

    def find_unique_values(self):
        """Find the total number of unique Product_Category, Sub_Category, and Product."""
        product_categories = self.df['Product_Category'].nunique()
        sub_categories = self.df['Sub_Category'].nunique()
        products = self.df['Product'].nunique()
        print(f"Total Product Categories: {product_categories}")
        print(f"Total Sub Categories: {sub_categories}")
        print(f"Total Products: {products}")


class DataVisualizer:
    """Handles data visualization tasks."""

    def __init__(self, dataframe):
        self.df = dataframe

    def plot_customer_age_histogram(self):
        """Plot a histogram for Customer_Age."""
        self.df['Customer_Age'].hist(bins=100, color='blue', edgecolor='black')
        plt.title("Customer Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Frequency")
        plt.show()

    def visualize_gender_distribution(self):
        """Visualize the gender distribution."""
        gender_counts = self.df['Customer_Gender'].value_counts()
        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.0f%%')
        plt.title("Gender Distribution")
        plt.show()

    def age_revenue_relationship(self):
        """Visualize the relationship between Age Group and Revenue."""
        plt.bar(self.df['Age_Group'], self.df['Revenue'], color='skyblue')
        plt.xlabel("Age Group")
        plt.ylabel("Revenue")
        plt.title("Relationship between Age Group and Revenue")
        plt.show()

    def max_min_profit_by_category(self):
        """Find max and min profit in Product Category and visualize."""
        max_profit = self.df.groupby('Product_Category')['Profit'].max()
        min_profit = self.df.groupby('Product_Category')['Profit'].min()
        print(f"Max Profit:\n{max_profit}\n")
        print(f"Min Profit:\n{min_profit}\n")
        max_profit.plot(kind='barh', color='green', label='Max Profit')
        plt.xlabel("Profit")
        plt.title("Max Profit by Product Category")
        plt.legend()
        plt.show()

    def monthly_revenue_profit(self):
        """Calculate and visualize monthly revenue and profit."""
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        monthly_data = self.df.groupby(self.df['Date'].dt.to_period('M')).agg({'Revenue': 'sum', 'Profit': 'sum'}).reset_index()
        monthly_data['Date'] = monthly_data['Date'].dt.to_timestamp()
        start_date = input("enter start mont with year in this format ex :2013-01")
        end_date = input("enter start mont with year in this format ex :2014-01")

        # Filter data for the specified range
        filtered_data = monthly_data[(monthly_data['Date'] >= start_date) & (monthly_data['Date'] <= end_date)]

        # Plotting revenue and profit trends
        plt.figure(figsize=(12, 6))
        plt.plot(filtered_data['Date'], filtered_data['Revenue'], label='Revenue', marker='o', color='blue')
        plt.plot(filtered_data['Date'], filtered_data['Profit'], label='Profit', marker='s', color='green')

        # Add labels, title, legend, and grid
        plt.xlabel('Month-Year')
        plt.ylabel('Amount')
        plt.title('Revenue and Profit Trends')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Show the plot
        plt.show()

    def profit_margin_per_product(self):
        """Calculate average profit margin per product and visualize."""
        self.df['profit_margin'] = (self.df['Revenue'] - self.df['Cost']) / self.df['Revenue']
        avg_margin = self.df.groupby('Product')['profit_margin'].mean().reset_index()
        plt.scatter(avg_margin['Product'], avg_margin['profit_margin'], color='blue', alpha=0.7)
        plt.xlabel("Product")
        plt.ylabel("Average Profit Margin (%)")
        plt.title("Average Profit Margin per Product")
        plt.xticks(rotation=90)
        plt.show()


if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv('sales.csv')

    # Preprocessing
    preprocessor = DataPreprocessor(df)
    preprocessor.visualize_missing_values()
    preprocessor.dataset_info()

    # Analysis
    analyzer = DataAnalyzer(df)
    analyzer.calculate_summary_statistics()
    analyzer.find_unique_values()

    # Visualization
    visualizer = DataVisualizer(df)
    visualizer.plot_customer_age_histogram()
    visualizer.visualize_gender_distribution()
    visualizer.age_revenue_relationship()
    visualizer.max_min_profit_by_category()
    visualizer.monthly_revenue_profit()
    visualizer.profit_margin_per_product()
