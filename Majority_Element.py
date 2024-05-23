# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


from collections import Counter
nums = [1,2]
c = Counter(nums)

for key,value in c.items():
    max_element = max(c.items(), key=lambda item: item[1])[0]
    ls = [max_element]
    
print(ls)

