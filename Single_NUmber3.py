# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]
# Example 3:

# Input: nums = [0,1]
# Output: [1,0]
from collections import Counter

new=[]
nums = [1,2,1,3,2,5]
c = Counter(nums)
print(c)


for key,value in c.items():
    if value ==1:
        new.append(key)
print(new)
        
