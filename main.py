from yahoo_data_fetcher import get_price

tickers = ["DIS", "KO", "PEP", "INTC", "F", "V"]

for t in tickers:
    get_price(ticker=t, verbose=True)