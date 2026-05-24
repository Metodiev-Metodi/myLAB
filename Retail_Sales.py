import pandas as pd
import matplotlib.pyplot as plt
# 1. Read Data: Load the CSV data into a Pandas DataFrame.
class RetailSalesAnalyzer:
  def __init__(self):
    self.data = pd.read_csv('retail_sales.csv')
    self.data['Date'] = pd.to_datetime(self.data['Date'])
# 2. Data Cleaning:
#      Check for and remove rows with missing values in any column.
  def data_clean(self):
    self.data.dropna(inplace=True)
# 3. Data Manipulation and Analysis:
#      Calculate total sales per product.
  def total_sales_per_product(self):
    return self.data.groupby('Product')['Sales'].sum()
#      Identify the best-selling product.
  def best_selling_product(self):
    return self.total_sales_per_product().sort_values(ascending=False).index[0]
#      Compute average daily sales.
  def average_daily_Sales(self):
    return self.data['Sales'].mean()
# 4.  Visualization:
#      Plot sales trends over time.
  def plot_sales_trend(self):
    self.data.groupby('Date')['Sales'].sum().plot(kind='line')
    plt.title('Sales Trend over Time')
    plt.xlabel('Date')
    plt.ylabel('Total sales')
    plt.show()
#      Display sales per product in a bar chart.
  def plot_sales_per_product(self):
    self.total_sales_per_product().plot(kind='bar')
    plt.title(" Sales Per Product")
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.show()



# 5.  Class and Function:
#      Define a Python class RetailSalesAnalyzer with methods for each of the above tasks (loading data, calculating statistics, and creating visualizations).
analyzer = RetailSalesAnalyzer()
print(' Total Sales per Product: \n', analyzer.total_sales_per_product())
print('Best Selling Product: ', analyzer.best_selling_product())
print(' Average Daily Sales ', analyzer.average_daily_Sales())
analyzer.plot_sales_per_product()
analyzer.plot_sales_trend()
