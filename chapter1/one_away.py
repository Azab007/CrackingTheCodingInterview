def one_away(s1,s2):
    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len == s2_len:
        return same_length_algorithm(s1,s2,s1_len)
    elif abs(s1_len - s2_len) == 1:
        if s1_len < s2_len:
            return one_diff_algorithm(s1,s2)
        else:
            return one_diff_algorithm(s2,s1)
    else:
        return False


def same_length_algorithm(s1,s2,size):
    c = 0
    for i in range(size):
        if s1[i] != s2[i]:
            c+=1
            if c > 1:
                return False
    return True

def one_diff_algorithm(s1,s2):
    i1,i2,c = 0,0,0
    for _ in range(len(s1)):
        if s1[i1] == s2[i2]:
            i1+=1
            i2+=1
        else:
            i2+=1
            c+=1
            if c > 1:
                return False
    return True
if __name__=="__main__":
    s1,s2 = input("Enter the String: ").split(",")
    print(one_away(s1,s2))