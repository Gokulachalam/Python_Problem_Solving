 

# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

# from collections import Counter
# nums = [1,2,3,2,3]
# new = []
# c = Counter(nums)
# print(c)
# for key,values in c.items():
#     if values == values:
#         new.append(key)
# print(new)



# from collections import Counter

# nums = [1, 2, 3, 2, 3]
# new = []
# c = Counter(nums)
# print(c)

# for key, value in c.items():
#     if value == value:  
#         new.append(key)

# print(new)    



from collections import Counter


nums = [1, 2, 3, 2]
sum = 0
c = Counter(nums)
for key,value in c.items():
    if value==1:
        sum+=key
print(sum)
