"""
Determine if a string is palindrome
"""
import re

def palindrome(s):
    # Convert to lower chars
    lower_s = s.lower()
    # Remove special chars: , ! blank
    lower_s = re.sub(r"[,!@ ]", "", lower_s)
    #lower_s = lower_s.replace(" !", "")
    print("Convert to lower case: ", lower_s)
    length = len(lower_s)
    for i in range(0, length//2):
        if lower_s[i] != lower_s[-(i + 1)]:
            return False

    return True

def palindrome2(s):
    rev = ""
    for i in s[len(s)//2:len(s)]:
        # Create a reverse string by append characters to the beginning
        rev = i + rev
        print(rev)
        #if rev == s:
        #    return True

    if s[0:len(s)//2] == rev:
        return True
    else:
        return False

    #return False

# Test code
print(palindrome("Aba"))
taco = "Tacocat !"
print("taco =", taco)
print(palindrome(taco))

s = "aabbaa"
print(palindrome2(s))