"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k."""

def subarraySum(nums, k):
    res = 0
    curSum = 0
    prefixSum = {0 : 1}
    
    for num in nums:
        curSum += num
        diff = curSum - k
        res += prefixSum.get(diff,0)
        prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
        
    return res

print(subarraySum([1,1,1],2))