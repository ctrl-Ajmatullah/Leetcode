def processStr(s):
    """Given a string s, process the string according to the following rules:
    - If the character is '*', delete the previous character (if any).
    - If the character is '#', duplicate the current string.
    - If the character is '%', reverse the current string.
    - Otherwise, append the character to the current string."""
    
    special = ['*', '#', "%"]
    result = []
    for char in s:
        if char in special:
            if char == '*':
                if len(result)>0:
                    result.pop()
            elif char == '#':
                result+=result
            else:
                result = result[::-1]
        else:
            result.append(char)

    return "".join(result)

result = processStr("z*#")
print(result)