# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

from collections import Counter

arr = [-3,0,1,-3,1,1,1,-3,10,0]
c = Counter(arr)
s = set()

for value in c.items():
    if value in s:
        print("false")

    s.add(value)
    print("true")