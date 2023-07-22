import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import streamlit as st

# Function to read data from MongoDB and create the DataFrame
def read_data_from_mongodb(symbol):
    # Connection string for the MongoDB database
    connection_string = 'mongodb://localhost:27017/New'

    # Connect to MongoDB
    client = pymongo.MongoClient(connection_string)

    # Access the database and collection
    db = client['New']
    collection = db['samples']

    # Query with a filter to retrieve data for the specified symbol
    data = list(collection.find({'symbol': symbol}))

    # Create a DataFrame from the retrieved data
    df = pd.DataFrame(data)

    # If the DataFrame contains a column named 'tradeDate', convert it to datetime and set it as the index
    if 'tradeDate' in df:
        df['tradeDate'] = pd.to_datetime(df['tradeDate'])
        df.set_index('tradeDate', inplace=True)

    return df

# Streamlit app
def main():
    st.title('Candlestick Chart for Stock Data')

    # Create a dropdown to select the symbol
    symbol = st.selectbox('Select a Symbol', ['BHARTIARTL', 'POWERGRID', 'ICICIBANK', 'ASIANPAINT', 'BRITANNIA', 'INFY', 'NTPC', 'CIPLA', 'ONGC', 'HDFCBANK', 
           'SUNPHARMA', 'EICHERMOT', 'TECHM', 'M&M', 'AXISBANK', 'RELIANCE', 'WIPRO', 'HINDALCO', 'HINDUNILVR', 'SBILIFE', 
           'ULTRACEMCO', 'APOLLOHOSP', 'HDFC', 'BAJAJFINSV', 'COALINDIA', 'DRREDDY', 'ITC', 'HEROMOTOCO', 'DIVISLAB', 'GRASIM', 
           'HCLTECH', 'TCS', 'UPL', 'KOTAKBANK', 'TATACONSUM', 'INDUSINDBK', 'JSWSTEEL', 'LT', 'SBIN', 'TATAMOTORS', 'HDFCLIFE', 
           'MARUTI', 'BPCL', 'TITAN', 'BAJFINANCE', 'ADANIPORTS', 'NESTLEIND', 'TATASTEEL', 'ADANIENT', 'BAJAJ-AUTO'])  # Add more symbols if needed

    # Read data from MongoDB for the selected symbol
    data = read_data_from_mongodb(symbol)

    # Define custom market colors for up and down candlesticks
    up_color = 'g'
    down_color = 'r'
    market_colors = mpf.make_marketcolors(up=up_color, down=down_color, inherit=True)

    # Create a custom style with the market colors
    mpf_style = mpf.make_mpf_style(marketcolors=market_colors)

    # Plot the candlestick graph using the custom style
    fig, ax = mpf.plot(data, type='candle', style=mpf_style, returnfig=True)

    # Show the interactive candlestick chart in Streamlit
    st.write(fig)

if __name__ == '__main__':
    main()