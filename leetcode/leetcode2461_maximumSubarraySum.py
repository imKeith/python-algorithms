from collections import defaultdict
def maximumSubarraySum(nums:list,k:int)->int:
    sum=0
    ans=0
    temp=defaultdict(int)
    for i,x in enumerate(nums):
        sum+=x
        temp[x] += 1
        left=i-k+1
        if left<0:
            continue
        if len(temp)==k:
            ans=max(ans,sum)

        out=nums[left]
        sum-=out
        temp[out]-=1
        if temp[out]==0:
            del temp[out]
    return ans