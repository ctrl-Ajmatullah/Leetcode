"""Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space."""

def firstMissingPositive(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    for j in range(len(nums)):
        val = abs(nums[j])
        if 1 <= val <= len(nums):
            if nums[val-1]>0:
                nums[val-1] *= -1
            elif nums[val-1] == 0:
                nums[val-1] = -1 * (len(nums)+1)

    for k in range(1, len(nums) + 1):
        if nums[k-1] >= 0:
            return k
    return len(nums) + 1     


print(firstMissingPositive([3,4,-1,1]))