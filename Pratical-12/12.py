import pandas as pd

# Load your dataset
df = pd.read_csv('stock_data.csv')  # Update with your CSV file path

# Print keys
print("Dataset Keys:")
print(df.columns.tolist())

# Number of rows and columns
num_rows, num_cols = df.shape
print("\nNumber of Rows:", num_rows)
print("Number of Columns:", num_cols)

# Feature names
print("\nFeature Names:")
print(df.columns.tolist())

# Description of the dataset
print("\nDataset Description:")
print(df.describe(include='all'))
