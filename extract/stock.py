import yfinance as yf
import pandas as pd

ticker_symbol = '122870.KQ'

yg_stock = yf.Ticker(ticker_symbol)

historical_data = yg_stock.history(period='1mo')

csv_filename = 'YG Entertainment Stock Data.csv'

historical_data.to_csv(csv_filename)

print(f"Data saved to {csv_filename}")