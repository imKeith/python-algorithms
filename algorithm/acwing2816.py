n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i,j=0,0
cnt=0
while i<m and j<n:
    if a[j]==b[i]:
        i+=1
        j+=1
        cnt+=1
        print(a[j],b[i],cnt)
    else:
        i+=1
if cnt==n:
    print("Yes")
else:
    print("No")