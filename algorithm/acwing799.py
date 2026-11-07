n=int(input())
num=list(map(int,input().split()))
cnt=[0]*100001
left,ans=0,0
for right in range(n):
    cnt[num[right]]+=1
    while cnt[num[right]]>1:
        cnt[num[left]]-=1
        left+=1
    ans=max(ans,right-left+1)
print(ans)