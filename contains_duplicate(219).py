"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

def containsNearbyDuplicate(nums,k):
    window = set()
    l = 0
    
    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1
        
        if nums[r] in window:
            return True
        window.add(nums[r])
    
    return False

print(containsNearbyDuplicate([1,0,1,1],1))