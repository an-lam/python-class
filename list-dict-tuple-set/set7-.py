# set7.py
# Create a program that takes some text and returns a list of all
# the characters in the text that are not vowels, sorted in
# alphabetical order.

my_text = "The chAracters in the text that are not vowels"

vowels = frozenset("AIEOUaieou")
print(vowels)
"""
my_set = set(my_text)
print(my_set)
no_vowels = my_set.difference(vowels)
print(no_vowels)
"""
filtered_text = set(my_text).difference(vowels)
print(filtered_text)

sorted_text = sorted(filtered_text)
print(sorted_text)