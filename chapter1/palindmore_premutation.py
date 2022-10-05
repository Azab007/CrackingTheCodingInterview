from collections import Counter
import string

def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]

def palindmore_permutation(s):
    c = Counter(s)
    return sum(x%2 for x in c.values()) <=1


if __name__=="__main__":
    s = input("Enter the string: ")
    s = clean_phrase(s)
    if palindmore_permutation(s):
        print("the string is a permutation of a palindmore")
    else:
        print("the string is not a permutation of a palindmore")