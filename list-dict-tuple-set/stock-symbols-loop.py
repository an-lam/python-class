stocks = {"AAPL": "Apple Inc., sells expensive toys",
         "NFLX": "Netflix, sells streaming movies",
         "AMZN": "Amazon, sells everything",
         "BYND": "Beyond Meat, vegetarian",
          "FB": "Facebook, sells nothing, but makes lots of money"}

print("original stocks: {}".format(stocks))

while True:
    dict_key = input("Please enter a stock symbol: ")
    if dict_key == "quit" or dict_key == "q":
        break

    #description = stocks.get(dict_key)
    #print(description)
    if dict_key in stocks:
        #description = stocks.get(dict_key)
        description = stocks[dict_key]
        print(description)
    else:
        print("We don't have a " + dict_key)

print("End of program")