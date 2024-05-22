# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

l1 = [2,4,3]
l2 = [5,6,4]


# Convert each element to string and join them
result = ''.join(map(str, l1))
result2 = ''.join(map(str,l2))

print(result)  # Output: "243"
print(result2)
c = int(result)
d = int(result2)
print(c+d)