import sys
def sortStack(s):
    res = []
    buff = []
    while len(s) != 0:
        mn = sys.maxsize
        while len(s) != 0:
            tmp = s.pop()
            if mn > tmp:
                mn = tmp
            buff.append(tmp)
        res.append(mn)
        flag = False
        while len(buff) != 0:
            val = buff.pop()
            if val != mn or (val == mn and flag):
                s.append(val)
            elif val == mn:
                flag=True


    return res
if __name__=="__main__":
    s = [4,5,7,6,1,8,1]
    print(sortStack(s))
