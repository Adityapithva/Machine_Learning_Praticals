import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:/Praticals/Machine_Learning_Praticals/stock_data.csv')
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Open'], label='Open', color='blue')
plt.plot(df['Date'], df['High'], label='High', color='green')
plt.plot(df['Date'], df['Low'], label='Low', color='orange')
plt.plot(df['Date'], df['Close'], label='Close', color='red')

plt.plot(df['Date'], df['Volume'], label='Volume', color='gray', alpha=0.3)

plt.title('Stock Prices and Volume')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.show()
