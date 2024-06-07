# Example 1:

# Input: a = 2, b = [3]
# Output: 8
# Example 2:

# Input: a = 2, b = [1,0]
# Output: 1024
# Example 3:

# Input: a = 1, b = [4,3,3,8,5,2]
# Output: 1


a = 2147483647
b = [2,0,0]
result = int(''.join(map(str, b)))
ans = pow(a,result)
print(ans)


