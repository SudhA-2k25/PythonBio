# KMP
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = build_lps(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            
            if j == m:
                return i - j  # pattern found at index i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1  # pattern not found


# Example usage
text = "malayalam"
pattern = "laya"
index = kmp(text, pattern)

if index != -1:
    print("Pattern found at position :", index)
else:
    print("Pattern not found")