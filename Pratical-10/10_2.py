import pandas as pd
df = pd.read_csv('duplicate_data.csv');


# Remove duplicates
df_cleaned = df.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(df_cleaned)
