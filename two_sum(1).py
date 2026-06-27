def twoSum(nums, target):
    """Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target."""
    
    hash = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash:
            return [hash[complement], i]
        hash[num] = i

result = twoSum([2, 7, 11, 15], 9)
print(result)