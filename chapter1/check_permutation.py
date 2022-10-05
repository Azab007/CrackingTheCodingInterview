#O(NlogN) considiring N equals the max lengt of two strings
from collections import Counter

def check_premutation(s1,s2):
    return sorted(s1) == sorted(s2)
def check_permutation2(s1,s2):
    return Counter(s1) == Counter(s2)

if __name__=="__main__":
    s1 = input("Enter the first string: ")
    print('\n')
    s2 = input("Enter the second string: ")
    if check_permutation2(s1,s2):
        print("{} is a premutation of {}".format(s1,s2))
    else:
        print("{} is a not a premutation of {}".format(s1,s2))