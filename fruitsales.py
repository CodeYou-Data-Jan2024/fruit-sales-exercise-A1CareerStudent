import pandas as pd

# Read the CSV file
fruit_sales = pd.read_csv("fruit_sales.csv", index_col=0)

# Print the DataFrame
print(fruit_sales)
