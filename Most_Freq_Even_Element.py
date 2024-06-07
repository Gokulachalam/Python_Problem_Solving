# Example 1:

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.
# Example 2:

# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.
# Example 3:

# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.




# from collections import Counter

# nums = [4,4,4,9,2,4]
# mew = []
# new = []
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         new.append(nums[i])
#         c = Counter(new)
#         for key , value in c.items():
#             if value >1:
#                 mew.append(key)

# print(min(mew))







# Example 1:

# Input: nums = [1,3,6,10,12,15]
# Output: 9
# Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
# Example 2:

# Input: nums = [1,2,4,7,10]
# Output: 0
# Explanation: There is no single number that satisfies the requirement, so return 0.


nums = [1,2,4,7,10]
# nums = [1,3,6,10,12,15]
div=[]
tot = 0
for i in range(len(nums),0):
    print(i)
    # if nums[i]%3==0 and i%2 == 0:
    #     div.append(nums[i])
    #     s = int(sum(div)/2)
    #     print(s)
    # else:
    #     print("odd num in list")
