stocks = {"AAPL": "Apple Inc., sells expensive toys",
         "NFLX": "Netflix, sells streaming movies",
         "AMZN": "Amazon, sells everything",
         "BYND": "Beyond Meat, vegetarian",
          "FB": "Facebook, sells nothing, but makes lots of money"}

print("original stocks: {}".format(stocks))

print(stocks.keys())

ordered_keys = list(stocks.keys())
ordered_keys.sort()
print("ordered_keys = " + str(ordered_keys))

#ordered_keys = sorted(list(stocks.keys()))
print("stocks using ordered_keys:")
for symbol in ordered_keys:
    print(symbol + " - " + stocks[symbol])

print('-' * 40)
print("stocks using sorted key in place:")
for symbol in sorted(stocks.keys(), reverse=True):
    print(symbol  + " - " + stocks[symbol])

print('-' * 40)
print("stocks values only (no keys):")
for val in stocks.values():
    print(val)

print('-' * 40)
print("another way of printing keys:")
for value in stocks:
    print(value)

print("stocks keys only :")
stocks_keys = stocks.keys()
print(stocks_keys)

print("Add a new key-value pair:")
stocks["UBER"] = "Xe om idea from Vietnam"
print(stocks)

print("Change the value:")
stocks["FB"] = "Facebook: good for finding friends"
print(stocks)

s_tuple = tuple(stocks.items())
print("s_tuple:")
print(s_tuple)

print("Use tuple to break apart key-value in stocks")
for symbol in s_tuple:
    ticker, description = symbol
    # print(type(ticker))
    print(ticker + " is " + description)