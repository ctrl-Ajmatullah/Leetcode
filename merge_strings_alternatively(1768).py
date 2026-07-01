"""You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string"""

def mergeAlternately(word1, word2):
    res = ""
    i,j = 0,0
    while i < len(word1) and j < len(word2):
        res += word1[i] + word2[j]
        i += 1
        j += 1
    res += word1[i:] + word2[j:]
    return res

print(mergeAlternately("abc", "pq"))
        