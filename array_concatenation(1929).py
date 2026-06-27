def getConcatenation(nums):
    """
    Given an integer array nums of length n, you want to create an array ans of length 2n where
    ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

    Specifically, ans is the concatenation of two nums arrays.

    Return the array ans.

    :param nums: List[int] - The input array of integers.
    :return: List[int] - The concatenated array.
    """
    nNums = nums[::]
    for num in nums:
        nNums.append(num)
    return nNums

result = getConcatenation([1, 2, 3])
print(result)
    