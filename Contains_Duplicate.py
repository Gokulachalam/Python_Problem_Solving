# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from collections import Counter
nums =[2,14,18,22,22]
new=[]
# c = Counter(nums)
# for key,values in c.items():
#     if values == 1:
#         new.append(values)

# print(new)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            new.append(nums[i])
            new.append(nums[j])
print(new)















