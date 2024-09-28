import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
}

print(pd.DataFrame(data).drop(columns=['age']));