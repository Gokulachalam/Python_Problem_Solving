# Example 1:

# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Explanation:
# The element sum of nums is 1 + 2 + 3 + 4 = 10.
# The digit sum of nums is 1 + 2 + 3 + 4 = 10.
# The absolute difference between the element sum and digit sum is |10 - 10| = 0.


nums = [2,7,8,10,8,10,1,10,5,9]
first = sum(nums)
print(first)


conv = list(map(str,nums))
c = ''.join(conv)

s = str(c)

final = list(map(int,s))
second = sum(final)
print(second)


print(abs(second-first))


