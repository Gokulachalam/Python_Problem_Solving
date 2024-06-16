# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.






#gpt explanation - https://chatgpt.com/c/6b8611a0-48b2-44c9-be6d-f5d6d4474a04

nums = [-2,1,-3,4,-1,2,1,-5,4]
current_sum = nums[0]
global_sum = nums[0]
for i in nums[1::]:
    current_sum = max(i,current_sum+i)
    global_sum = max(global_sum,current_sum)
print(global_sum)




