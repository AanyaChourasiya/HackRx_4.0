import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import streamlit as st
import time

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

# Function to update the candlestick chart
def update_candlestick_chart(symbol):
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

# Streamlit app
def main():
    st.title('Real-time Candlestick Chart for Stock Data')

    # Create a multiselect to select multiple symbols
    selected_symbols = st.multiselect('Select Symbols', 
                                      ['ADANIENT', 'ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SUNPHARMA', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'ULTRACEMCO', 'UPL', 'WIPRO'])

    # Update the candlestick chart for each selected symbol
    for symbol in selected_symbols:
        # st.subheader(f'Candlestick Chart for {symbol}')
        update_candlestick_chart(symbol)
        time.sleep(5)  # Adjust the interval as needed

if __name__ == '__main__':
    main()