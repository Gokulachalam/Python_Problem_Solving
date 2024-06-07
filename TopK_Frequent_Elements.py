# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import Counter
nums = [1,1,1,2,2,3]
k = 2
c = Counter(nums)
for key, value in c.items():
    if value >=k:
        print(value)

#