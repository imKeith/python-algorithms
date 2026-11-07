n,m,q=map(int,input().split())
num=[]
for i in range(n):
    row=list(map(int,input().split()))
    num.append(row)
# print(num)
diff=[[0 for j in range(m+1)]for i in range(n+1)]
for i in range(q):
    x1,y1,x2,y2,c=map(int,input().split())
    diff[x1 - 1][y1 - 1] += c
    diff[x1 - 1][y2] -= c
    diff[x2][y1 - 1] -= c
    diff[x2][y2] += c
s=[[0 for j in range(m+2)]for i in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j]=s[i][j-1]+s[i-1][j]-s[i-1][j-1]+diff[i-1][j-1]
        num[i-1][j-1]+=s[i][j]

for row in num:
    print(*row)