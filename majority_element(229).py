"""Given an integer array of size n, 
find all elements that appear more than ⌊n / 3⌋ times."""

def majorityElement(nums):
    
    map = {}
    for num in nums:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
                
    res = []
    for key in map:
        if map[key] > len(nums)//3:
            res.append(key)
    return res

print(majorityElement([1,2]))