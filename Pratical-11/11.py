import pandas as pd

df = pd.read_csv('data.csv')


print("\nRows with NaN values:")
print(df[df.isnull().any(axis=1)]) 
print("\nColumns with NaN values:")
print(df.columns[df.isnull().any()])  

df_cleaned = df.dropna()

print("\nDataFrame after dropping rows with any NaNs:")
print(df_cleaned)
