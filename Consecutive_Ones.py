# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
from collections import Counter
nums = [1,1,0,1,1,1]
new=[]
c = Counter(nums)
print(c)
# for key , value in c.items():

# #     if value==1:
# #         new.append(key)
# # print(new)