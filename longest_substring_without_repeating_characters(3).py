"""Given a string s, find the length of the longest substring without duplicate characters."""

def lengthOfLongestSubstring(s):
    window = set()
    l = 0
    longest = 0
    
    for r in range(len(s)):
        while s[r] in window:
            window.remove(s[l])
            l +=1
        window.add(s[r])
        longest = max(longest, len(window))
    return longest

print(lengthOfLongestSubstring("abcabcabc"))