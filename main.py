import yahoofinance as yf
import sys
import datetime

print(f"Using yfinance version: {yf}")
print(f"Python version: {sys.version}")

goog = yf.Ticker("GOOG")
# Get daily data for the last 5 years up to the last available trading day
goog_hist = goog.history(period="5y", interval="1d")
print("GOOG Daily Data (Last 5 days):")
print(goog_hist.tail())