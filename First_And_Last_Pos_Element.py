# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

nums = [5,7,7,8,8,10] 
target = 8
conv = []
for i in range(len(nums)):
    if nums[i] == target:
        conv.append(i)
print(conv)



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        conv = []
        for i in range(len(nums)):
            if nums[i] == target:
                conv.append(i)
                return conv

        return [-1,-1]
