# pip install yfinance
# pip install pandas-datareader
# pip install matplotlib

import yfinance as yf
import matplotlib

msft = yf.Ticker("MSFT")

msft.actions

