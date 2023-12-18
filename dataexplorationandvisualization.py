# Retail Store Data Analysis Report

## 1. Data Loading and Inspection:

### 1.1 Loading the Dataset:
python
import pandas as pd

# Assuming the dataset is in a CSV file named 'retail_data.csv'
df = pd.read_csv('retail_data.csv')


### 1.2 Initial Data Inspection:
python
# Display the first few rows of the dataset
print(df.head())

# Check the data types and missing values
print(df.info())


## 2. Data Cleaning:

### 2.1 Handling Missing Data:
python
# Identify and handle missing values
df.dropna(inplace=True)


### 2.2 Duplicate Entries:
python
# Check for and handle duplicate entries
df.drop_duplicates(inplace=True)


## 3. Data Exploration:

### 3.1 Basic Statistics:
python
# Calculate and summarize basic statistics
sales_stats = df['sales_revenue'].describe()
print(sales_stats)


### 3.2 Distribution Exploration:
python
# Explore the distribution of sales revenue and quantity sold
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df['sales_revenue'], bins=20, color='blue', alpha=0.7, label='Sales Revenue')
plt.xlabel('Sales Revenue')
plt.ylabel('Frequency')
plt.title('Distribution of Sales Revenue')
plt.legend()
plt.show()


### 3.3 Outlier Identification:
python
# Identify and handle outliers (example: using IQR method)
Q1 = df['sales_revenue'].quantile(0.25)
Q3 = df['sales_revenue'].quantile(0.75)
IQR = Q3 - Q1

# Remove outliers
df = df[(df['sales_revenue'] >= Q1 - 1.5 * IQR) & (df['sales_revenue'] <= Q3 + 1.5 * IQR)]


## 4. Data Visualization:

### 4.1 Monthly Trends:
python
# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract month from the 'date' column
df['month'] = df['date'].dt.month

# Plot monthly trends
monthly_trends = df.groupby('month')['sales_revenue'].sum()
monthly_trends.plot(kind='bar', color='green')
plt.xlabel('Month')
plt.ylabel('Total Sales Revenue')
plt.title('Monthly Trends in Sales Revenue')
plt.show()


### 4.2 Product Distribution:
python
# Plot the distribution of products across different categories
plt.figure(figsize=(12, 6))
df['product_category'].value_counts().plot(kind='bar', color='orange')
plt.xlabel('Product Category')
plt.ylabel('Number of Products Sold')
plt.title('Distribution of Products Across Categories')
plt.show()


### 4.3 Top-Selling Products/Categories:
python
# Identify and plot top-selling products or categories
top_products = df.groupby('product_id')['sales_revenue'].sum().nlargest(10)
top_products.plot(kind='bar', color='purple')
plt.xlabel('Product ID')
plt.ylabel('Total Sales Revenue')
plt.title('Top 10 Selling Products')
plt.show()


### 4.4 Correlations:
python
# Explore correlations between sales revenue and other variables
import seaborn as sns

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()