def stringCompression(s):
    if s == "":
        return ""
    cur = s[0]
    cnt=1
    res = ""
    for c in s[1:]:
        if c == cur:
            cnt+=1
        else:
            res+= str(cnt)+cur
            cur = c
            cnt=1
    res+= str(cnt)+cur
    return res if len(res) < len(s) else s
if __name__=="__main__":
    s = input("Enter the string: ")
    print(stringCompression(s))