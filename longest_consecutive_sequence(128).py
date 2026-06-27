"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""


def longestConsecutive(nums):
    
    numSet = set(nums)
    longest = 0
    
    for num in numSet:
        #check start of a sequence
        if (num - 1) not in numSet:
            length = 0
            while (num + length) in numSet:
                length += 1
            longest = max(longest,length)
    return longest

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))