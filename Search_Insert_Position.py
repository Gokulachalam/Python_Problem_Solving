# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


# nums = [1,3,5,6]
# target = 2
# length = len(nums)
# for i in range(length):
#     if nums[i] != target:
#         nums.append(target)
#         print(nums)




nums = [1, 3, 5, 6]
target = 7

nums.append(target)
nums.sort()
print(nums)
for i in range(len(nums)):
    if nums[i] == target:
        idx = nums.index(target)
print(idx)

