"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0."""

def threeSum(nums):
    res = []
    nums.sort()
    for i, n in enumerate(nums):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        while left < right:
            threeSum = n + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                res.append([n,nums[left],nums[right]])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
    return res

print(threeSum([-1,0,1,2,-1,-4]))
