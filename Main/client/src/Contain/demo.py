from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import mpld3

stock = pd.read_csv(r"C:\Users\Hp\OneDrive\Documents\SampleStockPrices.csv",index_col=7,parse_dates=True)
stock.head()

# Define the TIMEFRAMES list with available timeframe options
TIMEFRAMES = ['D5', 'D10', 'D15', 'D20', 'D25', 'MN1', 'W5', 'W6', 'W7']

# Define the TIMEFRAME_DICT to map human-readable labels to timeframe values
TIMEFRAME_DICT = {

     '05 Days': 'D5',
    '10 Days': 'D10',
    '15 Days': 'D15',
    '20 Days': 'D20',
    '25 Days': 'D25',
    '1 Month': 'MN1',
    '5 Weeks': 'W5',
    '6 Weeks': 'W6',
    '7 Weeks': 'W7',

    #  'D5':stock[stock['days']<=5],
    #  'D10':stock[stock['days']<=10],
    #  'D15':stock[stock['days']<=15],
    #  'D20':stock[stock['days']<=20],
    #  'D25':stock[stock['days']<=25],
    #  'MN1':stock[stock['days']<=30],
    #  'W5':stock[stock['days']<=35],
    #  'W6':stock[stock['days']<=42],
    #  'W7':stock[stock['days']<=49]
}

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

unique_symbols = stock['symbol'].unique()
symbol_dropdown = html.Div([
    html.P('Symbol:'),
    dcc.Dropdown(
        id='symbol-dropdown',
        options=[{'label': symbol, 'value': symbol} for symbol in unique_symbols],
        value='ADANIENT',
        multi=True
    )
])

timeframe_dropdown = html.Div([
    html.P('Timeframe:'),
    dcc.Dropdown(
        id='timeframe-dropdown',
        options=[{'label': timeframe, 'value': timeframe} for timeframe in TIMEFRAMES],
        value='D5'
    )
])

num_bars_input = html.Div([
    html.P('Number of Candles'),
    dbc.Input(id='num-bar-input', type='number', value='20')
])

app.layout = html.Div([
    html.H1('CandleStick Chart'),

    dbc.Row([
        dbc.Col(symbol_dropdown),
        dbc.Col(timeframe_dropdown),
        dbc.Col(num_bars_input)
    ]),

    html.Hr(),

    dcc.Interval(id='update', interval=200),

    html.Div(id='page-content')

], style={'margin-left': '5%', 'margin-right': '5%', 'margin-top': '20px'})

def mpl_to_html(fig):
   
    return mpld3.fig_to_html(fig)

@app.callback(
    Output('page-content', 'children'),
    Input('update', 'n_intervals'),
    State('symbol-dropdown', 'value'), State('timeframe-dropdown', 'value'), State('num-bar-input', 'value')
)
def update_ohlc_chart(interval, symbol, timeframe, num_bars):
    timeframe_str = timeframe
    timeframe = TIMEFRAME_DICT[timeframe]
    num_bars = int(num_bars)

    print(symbol, timeframe, num_bars)

    bars = stock.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    df = pd.DataFrame(bars)
    df['days'] = pd.to_datetime(df['days'], unit='s')
    df=df[df["symbol"]=="ADANIENT"]

    # Your matplotlib code for creating the candlestick graph goes here
    green_stock = df[df.close > df.open].copy()
    green_stock["Height"] = green_stock["close"] - green_stock["open"]

    red_stock = df[df.close < df.open].copy()
    red_stock["Height"] = red_stock["open"] - red_stock["close"]

    plt.style.use("fivethirtyeight")
    fig = plt.figure(figsize=(15, 7))

    ##Grey lines
    plt.vlines(x=green_stock["tradeDate"], ymin=green_stock["low"], ymax=green_stock["high"], color="green")

    plt.vlines(x=red_stock["tradeDate"], ymin=red_stock["low"], ymax=red_stock["high"], color="orangered")

    ##Green candles
    plt.bar(x=green_stock["tradeDate"], height=green_stock["Height"], bottom=green_stock["open"], color="green")

    ##Red candles
    plt.bar(x=red_stock["tradeDate"], height=red_stock["Height"], bottom=red_stock["close"], color="orangered")

    plt.xlabel("Trade Date")
    plt.ylabel("Price (Rs.)")
    plt.title("Candlestick Stock")

    plt.tight_layout()

    # Convert the matplotlib plot to HTML using mpl_to_html() and include it in the Dash app
    plt_html = mpl_to_html(fig)

    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.update_layout(yaxis={'side': 'right'})
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True

    return [
        html.H2(id='chart-details', children=f'{symbol} - {timeframe_str}'),
        dcc.Graph(figure=fig, config={'displayModeBar': False}),
        html.Div(plt_html, dangerously_set_inner_html=True)  # Add the matplotlib plot as an HTML component
        ]

if __name__ == '__main__':
    # starts the server
    app.run_server()