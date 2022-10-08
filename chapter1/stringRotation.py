def stringRotation(s1,s2):
    if len(s1) > 0 and len(s1) == len(s2):
        return s2 in s1+s1
    return False

if __name__=="__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(stringRotation(s1,s2))