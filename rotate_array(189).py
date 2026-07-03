"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""

def rotate(nums, k):
    k = k % len(nums)
    
    def reversal(l,r):
        while l < r:
            (nums[l], nums[r]) = (nums[r], nums[l])
            (l, r) = (l + 1, r - 1)
    
    reversal(0, len(nums)-1)
    reversal(0, k - 1)
    reversal(k, len(nums)-1)
    return nums
    
print(rotate([1,2,3,4,5,6,7],3))