n,m=map(int,input().split())
num=list(map(int,input().split()))
# for i in range(m):
#     l,r,c=map(int,input().split())
#     for j in range(l-1,r):
#         num[j]=num[j]+c
diff=[0]*(n+1)
for i in range(m):
    l,r,c=map(int,input().split())
    diff[l-1]=diff[l-1]+c
    diff[r]=diff[r]-c

for i in range(n):
    print("%d"%num[i]+diff[i],end=' ')