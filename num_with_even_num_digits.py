# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

nums = [12,345,2,6,7896]
count=0
new =[]
even=[]
for num in nums:
    new.append([num])

for dig in new:
    s = str(dig[0])
    l = len(s)
    even.append(l)
for k in range(len(even)):
    if even[k]%2==0:
        count=count+1
print(count)
