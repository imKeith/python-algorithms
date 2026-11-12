from collections import defaultdict


def maxSum(nums:list,m:int,l:int)->int:
    ans=s=0
    temp=defaultdict(int)
    for i,x in enumerate(nums):
        s+=x
        temp[x]+=1
        left=i-k+1
        if left<0:
            continue
        if len(temp)>=m:
            ans=max(ans,s)

        out=nums[left]
        s-=out
        temp[out]-=1
        if temp[out]==0:
            del temp[out]
    return ans
