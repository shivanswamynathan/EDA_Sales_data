# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('sales.csv')

df.head()

# Preprocessing

class  preprocessing:
    def __init__(self, df):
        self.df = df

    def Visualization(self):
        plt.figure(figsize=(8, 6))
        sns.heatmap(df.isnull(), cmap="viridis", cbar=False, yticklabels=False)
        plt.title("Missing Values Visualization")
        plt.xlabel("Columns")
        plt.ylabel("Rows")
        plt.show()
        self.df.isnull()
        self.df.info()

obj1 = preprocessing(df)
obj1.Visualization()

#Calculate summary statistics (mean, median, etc.) for numeric columns

class colums:
    def __init__(self, df):
        self.df = df
    def numeric (self):
      numeric_colums = self.df.select_dtypes(include=['number'])
      print(numeric_colums.head())

obj2 = colums(df)
obj2.numeric()

class summary_statistics:
  def __init__(self, df):
    self.df = df
  def mean_median_mode(self):
    numeric_colums = self.df.select_dtypes(include=['number'])
    column = numeric_colums.iloc[:, 2:]
    mean_value = column.mean()
    median_value = column.median()
    mode_value = column.mode()
    print(f"Mean : {mean_value}")
    print(f"Median : {median_value}")
    print(f"Mode : {mode_value}")
obj3 = summary_statistics(df)
obj3.mean_median_mode()

#Find the total number of Product_Category, Sub_Category, Product

class unique_values:
  def unique(self):
    total_product_categories = df['Product_Category'].nunique()
    total_sub_categories = df['Sub_Category'].nunique()
    total_products = df['Product'].nunique()

    print(f"Total Product Categories: {total_product_categories}")
    print(f"Total Sub Categories: {total_sub_categories}")
    print(f"Total Products: {total_products}")

obj4 = unique_values()
obj4.unique()

#Histogram for Customer_Age

class histogram:
  def __init__(self, df):
    self.df = df
  def hist(self):
    df['Customer_Age'].hist(bins=10000, color='blue', edgecolor='black')
    plt.title(" Customer Age")
    plt.xlabel("age")
    plt.ylabel("No.of people")
    plt.show()

obj5 = histogram(df)
obj5.hist()

#visualise gender distribution

class gender_distribution:
  def gender (self):
    gender_counts = df['Customer_Gender'].value_counts()
    print('Gender Counts')
    print(gender_counts)
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.0f%%')
    plt.title('Gender Distribution')
    plt.show()

obj6 = gender_distribution()
obj6.gender()

#Relationship between Age Group and Revenue
class relationship:
  def bar (self):
    plt.bar(df['Age_Group'], df['Revenue'], width=0.8, color=None, label=None, align='center')
    plt.xlabel('Age Group')
    plt.ylabel('Revenue')
    plt.title('Relationship between Age and Revenue.')
    plt.legend()
    plt.show()
obj7 = relationship()
obj7.bar()

#Max and Min Profit in Product Category

class max_min:
  def extrema (self):
    group_max = df.groupby('Product_Category')['Profit'].max()
    group_min = df.groupby('Product_Category')['Profit'].min()
    print(f"Max Profit : {group_max}")

    print(f"Min Profit :{group_min}")

    print(f"Sum of Profit :{group_max.sum()}")
    print(f"sum of min : {group_min.sum()}")

    plt.barh(group_max.index, group_max.values, color='skyblue')
    plt.xlabel('Maximum Profit ')
    plt.ylabel('Product Category')
    plt.title('Maximum Profit by Product Category')
    plt.legend()
    plt.show()

obj8 = max_min()
obj8.extrema()

group_max1 = df.groupby('Product')['Profit'].max()
plt.figure(figsize=(8,22))
plt.barh(group_max1.index, group_max1.values, color='skyblue')
plt.xlabel('Maximum Profit ')
plt.ylabel('Product')
plt.title('Maximum Profit by')
plt.legend()
plt.show()


#Monthly revenue and profit

df['Date'] = pd.to_datetime(df['Date'])

# Aggregate revenue and profit by month-year
monthly_data = df.groupby(df['Date'].dt.to_period('M')).agg({
    'Revenue': 'sum',
    'Profit': 'sum'
}).reset_index()
monthly_data['Date'] = monthly_data['Date'].dt.to_timestamp()  # Convert back to timestamp for plotting

# geting inpu for start and end date
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



#Average profit margin per product

df['profit_margin'] = (df['Revenue'] - df['Cost']) / df['Revenue']
df.head()

average_margin = df.groupby('Product')['profit_margin'].mean().reset_index()

plt.figure(figsize=(22,8))
plt.scatter(average_margin['Product'], average_margin['profit_margin'], color='blue', alpha=0.7)

plt.xlabel('Product')
plt.ylabel('Average Profit Margin (%)')
plt.title('Average Profit Margin per Product')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()



#Revenue distribution across each age group

years = sorted(df['Year'].unique())[:5]  # Get the first 5 years
age_groups = df['Age_Group'].unique()

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(20, 5), sharey=True)

for i, year in enumerate(years):
    # Filter data for the year
    year_data = df[df['Year'] == year]

    # Create a boxplot for the age groups
    axes[i].boxplot([year_data[year_data['Age_Group'] == age]['Revenue'] for age in age_groups],
                    labels=age_groups, patch_artist=True)
    axes[i].set_title(f"Year: {year}")
    axes[i].set_xlabel("Age Group")
    axes[i].tick_params(axis='x', rotation=90)

# Set a common y-axis label
fig.supylabel("Revenue Distribution")
fig.suptitle("Revenue Distribution Across Age Groups ", fontsize=16)
plt.tight_layout()
plt.show()




#Profit by Sub-Category within Product Categories

category_stats = df.groupby(['Product_Category', 'Sub_Category']).agg({
    'Revenue': 'sum',
    'Profit': 'sum'
}).reset_index()

# Pivot the data to prepare for a stacked bar chart
pivot_data = category_stats.pivot(index='Product_Category', columns='Sub_Category', values='Profit')  # Change to 'Revenue' if needed

# Plotting the stacked bar chart
pivot_data.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='tab20c')

# Add labels and title
plt.xlabel('Product Category')
plt.ylabel('Total Profit')  # Change to 'Total Revenue' if using Revenue
plt.title('Profit by Sub-Category within Product Categories')
plt.xticks(rotation=0)
plt.legend(title='Sub Category')
plt.tight_layout()

# Show the plot
plt.show()

plt.figure(figsize=(22, 8))

product_stats = df.groupby('Product').agg({'Profit': 'sum'}).reset_index()  # Calculate total profit per product

plt.scatter(
    average_margin['Product'],
    average_margin['profit_margin'],
    s=product_stats['Profit'] / 1000,  # Scale profit for marker size
    color='Green',
    alpha=0.7
)

# Add labels and title
plt.xlabel('Product')
plt.ylabel('Average Profit Margin (%)')
plt.title('Profit Margin vs Profit Amount per Product')
plt.xticks(rotation=90)  # Rotate product names for better readability
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()