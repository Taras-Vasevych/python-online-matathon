from collections import Counter

def isPalindrome(strng):
    unpaired_letters = sum(
        value % 2 
        for value in dict(Counter(strng)).values()
    )
    return unpaired_letters <= 1
