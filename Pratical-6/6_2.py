import pandas as pd;
data = {
    'col1':[10,20,30],
    'col2':[40,50,60]
};
df = pd.DataFrame(data);
s = df.iloc[:,0];
print(s);