def rotateMatrix(m):
    if len(m) == 0 or len(m) != len(m[0]):
        return False
    n = len(m)
    for i in range(n):
        for j in range(i,n):
            m[i][j],m[j][i] = m[j][i],m[i][j]
    return m

if __name__=="__main__":
    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(rotateMatrix(m))