def majorityElement(nums):
    """Given an array nums of size n return the majority element
    :In linear time and O(1) space 
    :Boyer Moore Algorithm"""
    
    count, res = 0, 0
    
    for num in nums:
        if count == 0:
            res = num
            count += 1
        elif res == num:
            count += 1
        elif res != num:
            count -= 1
    return res

result = majorityElement([3,2,3])
print(result)
    
    