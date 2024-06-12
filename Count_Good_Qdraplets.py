# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d
 

# Example 1:

# Input: nums = [1,2,3,6]
# Output: 1
# Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
# Example 2:

# Input: nums = [3,3,6,4,5]
# Output: 0
# Explanation: There are no such quadruplets in [3,3,6,4,5].




class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    for d in range(c+1,len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count = count+1
        return count

        