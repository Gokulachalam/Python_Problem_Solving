# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]


from collections import Counter
new=[]
nums = [1,2]
n = int(len(nums)/3)
c = Counter(nums)
for key,value in c.items():
    if value > n:
        new.append(key)
print(new)