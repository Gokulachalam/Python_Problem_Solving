# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
# Example 2:

# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".


from collections import Counter
num = "51230100"
new=[]
l = list(num)
for i in l:
    if i=='0':
        new.append(i)
print(type(new))


for k in new:
    l.remove(k)
print(l)