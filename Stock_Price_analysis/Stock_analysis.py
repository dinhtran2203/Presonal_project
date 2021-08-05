# pip install yfinance
# pip install pandas-datareader
# pip install matplotlib

import yfinance as yf
import matplotlib

msft = yf.Ticker('MSFT')

print(msft.recommendations)
print(msft.tickers.AAPL.history(period='1mo'))
