import pandas as pd
import matplotlib.pyplot as plt

# Sample stock price data as a dictionary (you can replace this with actual data)
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Open': [100, 102, 101, 104, 106],
    'Close': [105, 103, 102, 107, 108]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter data between two specific dates
start_date = '2023-01-02'
end_date = '2023-01-04'
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
df_filtered = df.loc[mask]

# Plotting the opening and closing prices
plt.figure(figsize=(10, 6))
plt.plot(df_filtered['Date'], df_filtered['Open'], label='Opening Price', marker='o')
plt.plot(df_filtered['Date'], df_filtered['Close'], label='Closing Price', marker='o')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Opening and Closing Stock Prices Between Two Dates')

# Add legend
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()
