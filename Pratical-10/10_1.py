import pandas as pd

df = pd.read_csv('sample_data.csv')

#
df_cleaned = df.dropna()

print("DataFrame after dropping missing values:")
print(df_cleaned)
