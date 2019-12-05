# continuebreak.py
shopping_list = ["orange", "apple", "egg", "spam", "bread"]
for item in shopping_list:
    print()
    if item == 'egg':
        break
        # continue
    print("Buy " + item)

#meal = ["egg", "bacon", "beans", "sausages"]
meal = ["egg", "bacon", "spam", "beans", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        # break
        continue
    else:
        print("I like {0}".format(item))

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it")
