import pandas as pd;
data = {
    'name': ['Bob', 'Charlie','Alice'],
    'age': [25, 30, 35],
};
df = pd.DataFrame(data);
print(df.sort_values(by='name'));