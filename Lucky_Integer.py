# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.

from collections import Counter
arr = [2,2,2,3,3]
c = Counter(arr)
for key , value in c.items():
    if key == value:
        print(key)
