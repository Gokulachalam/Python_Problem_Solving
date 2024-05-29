# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# nums = [1,2,3,4]
# new = []
# product = 1
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i]!=nums[j]:
#                 product = product * nums[i]
#                 print(product)


nums = [-1,1,0,-3,3]
new = []

for i in range(len(nums)):
    product = 1  # Reset product for each new i
    for j in range(len(nums)):
        if i != j:  # Only multiply if indexes are not t    he same
            product *= nums[j]
    new.append(product)

print(new)
