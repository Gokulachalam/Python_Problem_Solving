# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:

# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21


n = 4421
l = list(map(int,str(n)))
product = 1
sum = 0
for i in range(len(l)):
    product = product*l[i]


for j in range(len(l)):
    sum = sum+l[j]


    result = product - sum


print(product)
print(sum)
print(result)

