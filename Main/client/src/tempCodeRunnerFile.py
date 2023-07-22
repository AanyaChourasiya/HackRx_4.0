import pymongo
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
from matplotlib.animation import FuncAnimation
import time
import os

# Function to read the Excel file and create the DataFrame
# def read_excel_file():
#     data = pd.read_csv(r"/content/New.csv")
#     data['tradeDate'] = pd.to_datetime(data['tradeDate'])
#     data.set_index('tradeDate', inplace=True)
#     return data

def read_data_from_mongodb():
    # Connection string for the MongoDB database
    connection_string = 'mongodb://localhost:27017/New'

    # Connect to MongoDB
    client = pymongo.MongoClient(connection_string)

    # Access the database and collection
    db = client['New']
    collection = db['samples']

    # Read data from MongoDB and create the DataFrame
    # Replace this with your logic to fetch data from MongoDB based on your schema
    data = list(collection.find({}))  # Example: Fetch all documents from the collection
    df = pd.DataFrame(data)
    # If the DataFrame contains a column named 'tradeDate', convert it to datetime and set it as the index
    if 'tradeDate' in df:
      df['tradeDate'] = pd.to_datetime(df['tradeDate'])
      df.set_index('tradeDate', inplace=True)

      # print(df.head())

      return df

# Create the initial DataFrame
data = read_data_from_mongodb()
# data['open'] = pd.to_numeric(data['open'], errors='coerce')
# data['high'] = pd.to_numeric(data['open'], errors='coerce')
# data['low'] = pd.to_numeric(data['open'], errors='coerce')
# data['close'] = pd.to_numeric(data['open'], errors='coerce')

# Create a figure and initial candlestick plot
fig, ax = plt.subplots()

# Define custom market colors for up and down candlesticks
up_color = 'g'
down_color = 'r'
market_colors = mpf.make_marketcolors(up=up_color, down=down_color, inherit=True)

# Create a custom style with the market colors
mpf_style = mpf.make_mpf_style(marketcolors=market_colors)

# Plot the initial candlestick graph using the custom style
mpf.plot(data, type='candle', style=mpf_style, ax=ax)

# Set the interval for checking updates (in seconds)
update_interval = 5  # Check for updates every 5 seconds

def update_graph(i):
    # Update the DataFrame with new data from MongoDB
    data = read_data_from_mongodb()

    # Clear the current plot and redraw with the updated data
    ax.clear()
    mpf.plot(data, type='candle', style=mpf_style, ax=ax)

# Create the animation
ani = FuncAnimation(fig, update_graph, interval=update_interval)

# Show the animated plot
# plt.savefig(r"C:\Users\Aanya Chourasiya\OneDrive\Pictures\Graph Image")
plt.show()