import yfinance as yf

stock = yf.Ticker("AAPL")
info = stock.info
print(type(info))

# print(info.keys())
print(len(info))
print(info['shortNme'])
print(info['longName'])
print(info['currentPrice'])

# print(info[]'longBusinessSummary'])

# print(info['longBusinessSummary'].split())
print('iphone' in info['longBusinessSummary'].lower().split())

print('iPhone' in info['longBusinessSummary'])

print(info['city'])
# info['city'][0] = 'c'
info['city'] = 'Wellesley'
print(info['city'])

# print(tickers)

# prices = {'APPL': [252.53, 300]}