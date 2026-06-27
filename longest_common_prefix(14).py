def longestCommonPrefix(strs):
    """Find the longest common prefix string amongst an array of strings."""
    
    min_length_str = min(strs, key=len)
    flag = ""
    
    for i in range(len(min_length_str)):
        if all(s[i] == min_length_str[i] for s in strs):
            flag += min_length_str[i]
        else:
            break
    return flag

result = longestCommonPrefix(["flower","flow","flight"])
print(result)
