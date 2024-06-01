# # Example 1:

# # Input: nums = [1,2,3,1,1,3]
# # Output: 4
# # Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# # Example 2:

# # Input: nums = [1,1,1,1]
# # Output: 6
# # Explanation: Each pair in the array are good.
# # Example 3:

# # Input: nums = [1,2,3]
# # Output: 0
# nums = [1,2,3,1,1,3]
# new=[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j] and i<j:
#             new.append(nums[i])
#             new.append(nums[j])
# print(int(len(new)/2))









# Example 1:

# Input: nums = [13,23,12]

# Output: 4

# Explanation:
# We have the following:
# - The digit difference between 13 and 23 is 1.
# - The digit difference between 13 and 12 is 1.
# - The digit difference between 23 and 12 is 2.
# So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.

# Example 2:

# Input: nums = [10,10,10,10]

# Output: 0

# Explanation:
# All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.


nums=[13,23,12]
count=0
conv = list(map(int, ''.join(map(str, nums))))
new=[]
for i in range(len(conv)):
    for j in range(len(conv)):
        p=conv[j]-conv[i]

        if conv[i] or conv[j] == p:
            new.append(p)

print(p)


