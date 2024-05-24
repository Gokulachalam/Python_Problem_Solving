# Example 1:

# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.
# Example 2:

# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.
 
from collections import Counter
nums = [1,3,6,4,3,4,2,4,5,3,53,3,5,35,34,35,5,31,99,99]
c=Counter(nums)

new = []

for key,value in c.items():
    if value ==1:
        new.append(key)
print(max(new))
