# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

nums = [1,2,3]


if len(nums) ==2:
    print(max(nums))

nums.sort()

s = set(nums)

conv = list(s)
if len(conv) ==2 or len(conv) ==1:
    print(max(conv))
else:

    first = max(conv)
    conv.remove(first)


    second = max(conv)
    conv.remove(second)



    third = max(conv)


    print(third)