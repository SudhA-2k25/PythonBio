# Rabin-karp
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    
    # Iterate over each window of the text
    for i in range(n - m + 1):
        # Check if the current window matches the pattern
        if text[i:i+m] == pattern:
            return i  # pattern found at index i
    
    return -1  # pattern not found

# Example usage
text = "malayalam"
pattern = "laya"
index = rabin_karp(text, pattern)

if index != -1:
    print("Pattern found at position :", index)
else:
    print("Pattern not found")
