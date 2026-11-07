n,m,q=map(int,input().split())
a=[]
for _ in range(n):
    row=list(map(int,input().split()))
    a.append(row)
# print(a)
s=[[0 for j in range(m+1)]for i in range(n+1)]
# print(s)
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+a[i-1][j-1]
for i in range(q):
    x1,y1,x2,y2=map(int,input().split())
    print(s[x2][y2]-s[x2][y1-1]-s[x1-1][y2]+s[x1-1][y1-1])