import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': ['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06'],
    'Open': [100, 106, 111, 116, 121],
    'Close': [105, 110, 115, 120, 125]
}

df = pd.DataFrame(data)

plt.plot(df['Date'], df['Open'], label='Opening Price', color='blue')
plt.plot(df['Date'], df['Close'], label='Closing Price', color='red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Opening and Closing Stock Prices')

plt.show()
