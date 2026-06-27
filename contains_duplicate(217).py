def contains_duplicate(nums):
    """
    Check if the list contains any duplicates.

    :param nums: List of integers
    :return: True if any value appears at least twice in the list, False otherwise
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

result = contains_duplicate([1, 2, 3, 4, 4])
print(result)  