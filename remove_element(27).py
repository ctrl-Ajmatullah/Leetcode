def removeElement(nums, val):
    """Remove the given val from the list and return the k value"""
    k = 0   
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k+=1
    print(nums)
    return k

result = removeElement([3,2,2,3],3)
print(result)