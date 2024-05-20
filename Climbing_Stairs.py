# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


n = 2

if n ==0 or n == 1:
    result = 1

else:
    first , second = 1,1
    for i in range(2,n+1):
        first , second = first , first + second
        result = second
print(result)


