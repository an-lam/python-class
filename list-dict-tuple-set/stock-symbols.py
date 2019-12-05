stocks = {"AAPL": "Apple Inc., sells expensive toys",
         "NFLX": "Netflix, sells streaming movies",
         "AMZN": "Amazon, sells everything",
         "BYND": "Beyond Meat, vegetarian",
          "FB": "Facebook, sells nothing, but makes lots of money",
         9: "this is numberic key"}

desc = stocks["FB"]
print(desc)

stocks["AAPL"] = "a phone"
print(stocks)
print(stocks[9])
print(stocks["AMZN"])

stocks["GOOGL"] = "Alphabet"
print(stocks)

# Delete a specific entry
del stocks[9]
print(stocks)

# What happens if we do this?
del stocks
# Delete all entries
# stocks.clear()
print(stocks)
