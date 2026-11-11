def numOfSubarrays(arr:list,k:int,threshold:int)->int:
    ans=0
    cnt=0.0
    for i,x in enumerate(arr):
        cnt+=x
        left=i-k+1
        if left<0:
            continue
        if cnt/k >= threshold:
            ans+=1
        cnt-=arr[left]
    return ans