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

 # Max and Min Profit :
 The max_min class calculates and visualizes the maximum and minimum profit for each 'Product_Category' using horizontal bar chart.
 
 # Monthly Revenue and Profit :
 The code calculates and plots the monthly revenue and profit trends over a specified time period, allowing users to analyze sales performance over time.

 # Average Profit Margin per Product :
    1 Calculate Profit Margin
      - A new column 'profit_margin' is added to the DataFrame. 
      -Profit margin is calculated using the formula: (Revenue - Cost) / Revenue. This represents the percentage of revenue that is profit for each sale.
    2  Group by Product: 
     -The DataFrame is grouped by the 'Product' column. -The mean() function is used to calculate the average profit margin for each product within its group. -The results are stored in a new DataFrame called 
        average_margin.
    3 Visualization: 
    -A scatter plot is generated using matplotlib.pyplot. -The x-axis represents the 'Product', and the y-axis represents the 'Average Profit Margin (%)'. -Each point on the plot corresponds to a product and its 
      average profit margin. 
    -The size of each point can optionally be adjusted to represent another variable, such as the total profit amount for that product.
    
  # Revenue Distribution Across Each Age Group:
       Visual Comparison: The boxplots provide a visual way to compare revenue distributions across different age groups within each year, allowing quick identification of groups with higher or lower median       
                          revenue and variability in spending.

       Trend Identification: By examining the boxplots across years, you can spot trends in revenue generation for each age group, such as increasing or decreasing median revenue or changes in the spread of the                                data.

       Targeted Insights: This visualization offers insights that can be used for targeted marketing and sales strategies, enabling businesses to focus on age groups with higher revenue potential or adapt their                             approaches based on observed trends.
       
   # Profit by Sub-Category within Product Categories:
       - The code groups the data by 'Product_Category' and 'Sub_Category' and calculates the total profit for each sub-category within each product category.
       - The results are stored in the category_stats DataFrame.
       - The category_stats DataFrame is pivoted to create a table where product categories are rows, sub-categories are columns, and the values represent the total profit for each sub-category within the    corresponding product category.



