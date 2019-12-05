stocks = {"AAPL": "Apple Inc., sells expensive toys",
         "NFLX": "Netflix, sells streaming movies",
         "AMZN": "Amazon, sells everything",
         "BYND": "Beyond Meat, vegetarian",
          "FB": "Facebook, sells nothing, but makes lots of money"}
new_ipos = {"LYFT": "Competitor of UBER",
            "UBER": "Rideshare company"}

print("original stocks: {}".format(stocks))

print("before update:")
print(stocks)
stocks.update(new_ipos)
print("after update:")
print(stocks)

# If you don't want to change original dictionary, use copy()
new_stocks = new_ipos.copy()
new_stocks.update(stocks)
print("\noriginal stocks:")
print(new_ipos)
print("\nnew_stocks: ")
print(new_stocks)


print("End of program")