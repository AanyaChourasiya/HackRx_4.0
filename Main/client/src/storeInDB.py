# import pymongo
# import pandas as pd
# import matplotlib.pyplot as plt
# import mplfinance as mpf
# import streamlit as st
# import time
# import os

# # Function to read data from MongoDB and create the DataFrame
# def read_data_from_mongodb(symbol):
#     # Connection string for the MongoDB database
#     connection_string = 'mongodb://localhost:27017/New'

#     # Connect to MongoDB
#     client = pymongo.MongoClient(connection_string)

#     # Access the database and collection
#     db = client['New']
#     collection = db['samples']

#     # Query with a filter to retrieve data for the specified symbol
#     data = list(collection.find({'symbol': symbol}))

#     # Create a DataFrame from the retrieved data
#     df = pd.DataFrame(data)

#     # If the DataFrame contains a column named 'tradeDate', convert it to datetime and set it as the index
#     if 'tradeDate' in df:
#         df['tradeDate'] = pd.to_datetime(df['tradeDate'])
#         df.set_index('tradeDate', inplace=True)

#     return df

# # Function to update the candlestick chart
# def update_candlestick_chart(symbol, save_path):
#     # Read data from MongoDB for the selected symbol
#     data = read_data_from_mongodb(symbol)

#     # Define custom market colors for up and down candlesticks
#     up_color = 'g'
#     down_color = 'r'
#     market_colors = mpf.make_marketcolors(up=up_color, down=down_color, inherit=True)

#     # Create a custom style with the market colors
#     mpf_style = mpf.make_mpf_style(marketcolors=market_colors)

#     # Plot the candlestick graph using the custom style
#     fig, ax = mpf.plot(data, type='candle', style=mpf_style, returnfig=True)

#     # Save the figure as an image
#     image_path = os.path.join(save_path, f"{symbol}_candlestick_chart.png")
#     fig.savefig(image_path)
#     plt.close(fig)

#     # Show the interactive candlestick chart in Streamlit
#     st.write(fig)

#     return image_path

# # Streamlit app
# def main():
#     st.title('Real-time Candlestick Chart for Stock Data')

#     # Create a multiselect to select multiple symbols
#     selected_symbols = st.multiselect('Select Symbols', 
#                                       ['BHARTIARTL', 'POWERGRID', 'ICICIBANK', 'ASIANPAINT', 'BRITANNIA', 'INFY', 'NTPC', 'CIPLA', 'ONGC', 'HDFCBANK', 
#                                        'SUNPHARMA', 'EICHERMOT', 'TECHM', 'M&M', 'AXISBANK', 'RELIANCE', 'WIPRO', 'HINDALCO', 'HINDUNILVR', 'SBILIFE', 
#                                        'ULTRACEMCO', 'APOLLOHOSP', 'HDFC', 'BAJAJFINSV', 'COALINDIA', 'DRREDDY', 'ITC', 'HEROMOTOCO', 'DIVISLAB', 'GRASIM', 
#                                        'HCLTECH', 'TCS', 'UPL', 'KOTAKBANK', 'TATACONSUM', 'INDUSINDBK', 'JSWSTEEL', 'LT', 'SBIN', 'TATAMOTORS', 'HDFCLIFE', 
#                                        'MARUTI', 'BPCL', 'TITAN', 'BAJFINANCE', 'ADANIPORTS', 'NESTLEIND', 'TATASTEEL', 'ADANIENT', 'BAJAJ-AUTO'])

#     # Folder to store the generated images
#     save_path = "Graph_Images"
#     os.makedirs(save_path, exist_ok=True)

#     # Update the candlestick chart for each selected symbol
#     for symbol in selected_symbols:
#         st.subheader(f'Candlestick Chart for {symbol}')
#         image_path = update_candlestick_chart(symbol, save_path)
#         st.image(image_path)

# if __name__ == '__main__':
#     main()



import streamlit as st
import os
from PIL import Image

# Streamlit app
def main():
    st.title('Real-time Candlestick Chart for Stock Data')

    # Create a multiselect to select multiple symbols
    selected_symbols = st.multiselect(
        'Select Symbols',
        ['BHARTIARTL', 'POWERGRID', 'ICICIBANK', 'ASIANPAINT', 'BRITANNIA', 'INFY', 'NTPC', 'CIPLA', 'ONGC', 'HDFCBANK',
         'SUNPHARMA', 'EICHERMOT', 'TECHM', 'M&M', 'AXISBANK', 'RELIANCE', 'WIPRO', 'HINDALCO', 'HINDUNILVR', 'SBILIFE',
         'ULTRACEMCO', 'APOLLOHOSP', 'HDFC', 'BAJAJFINSV', 'COALINDIA', 'DRREDDY', 'ITC', 'HEROMOTOCO', 'DIVISLAB', 'GRASIM',
         'HCLTECH', 'TCS', 'UPL', 'KOTAKBANK', 'TATACONSUM', 'INDUSINDBK', 'JSWSTEEL', 'LT', 'SBIN', 'TATAMOTORS', 'HDFCLIFE',
         'MARUTI', 'BPCL', 'TITAN', 'BAJFINANCE', 'ADANIPORTS', 'NESTLEIND', 'TATASTEEL', 'ADANIENT', 'BAJAJ-AUTO'])

    # Folder to fetch the generated images
    save_path = "Graph_Images"

    # List to store the images
    images = []

    # Fetch the images for each selected symbol
    for symbol in selected_symbols:
        image_path = os.path.join(save_path, f"{symbol}_candlestick_chart.png")

        # Check if the image exists and add it to the list
        if os.path.exists(image_path):
            images.append(Image.open(image_path))

    # Concatenate the images horizontally into a single image
    if images:
        merged_image = Image.new("RGB", (sum(img.width for img in images), max(img.height for img in images)))
        x_offset = 0
        for img in images:
            merged_image.paste(img, (x_offset, 0))
            x_offset += img.width

        # Show the merged image in Streamlit
        st.image(merged_image)

if __name__ == '__main__':
    main()