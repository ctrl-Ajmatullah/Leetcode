def sortArray(nums):
    """Sorts an array of integers in ascending order
    :Time complexity: O(n log n)"""
    
    return mergeSort(nums)

def mergeSort(nums):
    
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    
    l = mergeSort(nums[:mid])
    r = mergeSort(nums[mid:])
    
    res = merge(l,r)
    return res

def merge(l,r):
    (m,n) = (len(l),len(r))
    
    (target,i,j,k) = ([],0,0,0)
    
    while k < m + n:
        if i == m:
            target.extend(r[j:])
            k = k + (n - j)
        elif j == n:
            target.extend(l[i:])
            k = k + (n - i)
        elif l[i] < r [j]:
            target.append(l[i])
            (i,k) = (i+1, k+1)
        else:
            target.append(r[j])
            (j,k) = (j+1, k+1)
            
    return target


sorted_list = sortArray([21,34,12,56,32])
print(f"The sorted list is {sorted_list}")