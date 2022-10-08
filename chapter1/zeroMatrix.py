def zeroMatrix(m):
    r,c = len(m),len(m[0])
    rows = [0]*r
    cols = [0]*c
    for i in range(r):
        for j in range(c):
            if m[i][j] == 0:
                rows[i] = 1
                cols[j] = 1
    for i in range(r):
        if rows[i] == 1:
            nullifyRow(m,i,c)
    for j in range(c):
        if cols[j] == 1:
            nullifyCols(m,j,r)
    return m

def nullifyRow(m,i,c):
    for k in range(c):
        m[i][k] = 0

def nullifyCols(m,j,r):
    for k in range(r):
        m[k][j] = 0

if __name__=="__main__":
    s = [[1,2,3],[0,4,5],[2,6,8]]
    print(zeroMatrix(s))