import yfinance as yf

df = yf.Ticker("AAPL").history(period="1mo")
print(df[["Close"]].head())
print(f"Rows: {len(df)}")