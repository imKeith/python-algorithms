n,m,x=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
"""
for i in range(n):
    for j in range(m):
        if a[i]+b[j]==x:
            print("%d %d"%(i,j))
"""
i,j=0,m-1
while i<n and j>=0:
    s=a[i]+b[j]
    if s>x:
        j-=1
    elif s<x:
        i+=1
    else:
        print("%d %d"%(i,j))
        break