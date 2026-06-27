"""Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings"""

def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res
        

def decode(strs):
    res, i = [], 0
    
    while i < len(strs):
        j = i
        while strs[j] != "#":
            j += 1
        length = int(strs[i:j])
        
        res.append(strs[j+1:j+1+length])
        
        i = j + 1 + length