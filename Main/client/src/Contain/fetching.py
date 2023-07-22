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