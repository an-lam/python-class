def print_hello():
    print("Hello world!")
    return 2

def print_fruits():
    width = 80
    text = "apple and orange"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

# Parameter: text
def centre_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

print_hello()
print(print_hello())

# call the function
centre_text("")
centre_text("apple")
centre_text(12)
centre_text("orange")

