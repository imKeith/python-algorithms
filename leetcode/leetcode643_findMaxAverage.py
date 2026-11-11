

def findMaxAverage(nums:list,k:int)->float:
    ans = float('-inf')
    cnt = 0.0
    for i, x in enumerate(nums):
        cnt += x
        left = i - k + 1
        if left < 0:
            continue

        ans = max(cnt/k, ans)
        cnt -= nums[left]

    return ans