# power set
def power_set(s):
    # Initialize power set with empty set
    power = [[]]
    
    # Generate power set by adding each element to each subset in power set
    for i in s:
        power += [subset + [i] for subset in power]
    return power

# Example 
set1 = {1, 2, 3}
for subset in power_set(set1):
    print(subset)
