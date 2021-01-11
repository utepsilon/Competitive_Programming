def findPaths(m,path,i,j):
    r,c = len(m),len(m[0])
    # if destination is reached
    # print
    if i == r-1 and j == c-1:
        return path+[m[i][j]]
    

    # explore
    path.append(m[i][j])


    # move down
    if 0 <= i+1 <= r-1 and 0 <= j <= c-1:
        findPaths(m,path,i+1,j)


    # move right
    if 0 <= i <= r-1 and 0 <= j+1 <= c-1:
        findPaths(m,path,i,j+1)


    # move diagonal
    """
    if 0 <= i+1 <= r-1 and 0 <= j+1 <= c-1:
        findPaths(m,path,i+1,j+1)
    
"""
    # if none of the above is explorable or invalid index
    # backtrack
    path.pop()

t = int(input())
while(t>0):
    t-=1
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        x = input()
        mat.append([a for a in x])
    path = []
    p = findpaths(mat,path,0,0)
    print(p)
