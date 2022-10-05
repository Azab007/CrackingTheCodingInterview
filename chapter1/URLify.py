def URLify(s,l):
    return s[:l].replace(" ","%20")

if __name__=="__main__":
    s,l = input("Enter the string: ").split(",")
    l = int(l.strip())
    print(URLify(s,l))