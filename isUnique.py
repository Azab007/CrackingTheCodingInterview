def isUnique(s):
    st = set()
    for c in s:
        if c not in st:
            st.add(c)
        else:
            return False
    return True

def isUniqueWithoutDataStructure(s):
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

if __name__ == "__main__":
    s = input("Please Enter The String: ")
    unique = "Unique" if isUniqueWithoutDataStructure(s) else "Not Unique"
    print("The String is "+unique)