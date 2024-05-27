# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

# nums = [4,3,2,7,8,2,3,1]
# new = []
# for i in range(1,len(nums)+1):
#     if i!=nums[i]:
#         new.append(i)

# print(new)


# nums = [4,3,2,7,8,2,3,1]
# new = []
# res = []
# for i in range(1,len(nums)+1):
#     new.append(i)
#     for j in range(1,len(new)+1):
#         if new[j] not in nums[i]:
#             res.append(new[j])

# print(res)




nums = [4,3,2,7,8,2,3,1]
new = []
res = []

for i in range(1, len(nums) + 1):
    new.append(i) 

for i in new:
    if i not in nums:
        res.append(i)

print(res)


