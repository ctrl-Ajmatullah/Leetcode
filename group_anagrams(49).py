from collections import defaultdict

def groupAnagrams(strs):
    """Group anagrams from a list of strings."""
    
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord("a")] += 1
            
        res[tuple(count)].append(s)
        
    return res.values()

result = list(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(result)
    