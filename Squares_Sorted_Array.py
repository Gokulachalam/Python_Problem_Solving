# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 




nums = [-4,-1,0,3,10]
nums.sort()
new = []
for i in range(len(nums)):
    product = nums[i] * nums[i]
    new.append(product)
    new.sort()
print(new)




# my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# # Sorting the list in place
# my_list.sort()

# print("Sorted list:", my_list)
