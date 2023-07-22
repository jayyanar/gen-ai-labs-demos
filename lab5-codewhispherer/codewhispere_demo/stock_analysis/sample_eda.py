# Read in the CSV file name "all_stocks_5yr.csv" using pandas and store as varible df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('all_stocks_5yr.csv')
print(df.head())


# Print the first 10 rows
print(df.head(10))

# Print number of rows
print(df.shape[0])

# Remove the duplicate columns in date and print the number of row now
df.drop_duplicates(subset=['date'], inplace=True)
print(df.shape[0])

# create a plot using Matplotlib  with X-Axis and Y-Axis with legend and store as png
plt.plot(df['date'], df['close'])
plt.xlabel('Date')
plt.ylabel('Close')
plt.legend(['AAPL'])
plt.savefig('AAPL.png')