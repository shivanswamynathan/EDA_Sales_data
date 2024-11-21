# Report on Sales Data Analysis
# Data Loading and Preprocessing:
- The code starts by loading sales data from a CSV file ('sales_data - sales_data.csv') into a Pandas DataFrame.
- A visualization of missing values is created using a heatmap to identify potential data quality issues.
- The df.info() method is used to display basic information about the DataFrame, including data types and non-null values.

# Summary Statistics:
- The colums class is used to select numeric columns.
- The summary_statistics class calculates and prints the mean, median, and mode of numeric columns (excluding the first three columns, likely index or date-related) to understand the central tendency and distribution of the data.

 #  Unique Value Counts:
 The unique_values class calculates and prints the total number of unique values for 'Product_Category', 'Sub_Category', and 'Product' columns, providing insights into the variety of products sold.

 # Customer Age Distribution :
 The histogram class creates a histogram to visualize the distribution of 'Customer_Age', showing the frequency of different age groups among customers.

 # Gender Distribution:
 The gender_distribution class calculates and visualizes the distribution of 'Customer_Gender' using a pie chart, illustrating the proportion of male and female customers.

 # Relationship between Age and Revenue:
 The relationship class explores the relationship between 'Age_Group' and 'Revenue' using a bar chart, helping to identify potential trends in revenue generation across different age groups.

 #
