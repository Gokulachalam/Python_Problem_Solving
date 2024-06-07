# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

s = "cbacdcbc"
from collections import Counter
# c = Counter(s)

# for key,value in c.items():
#     if value 
# print(c)


c = set(s)
list_s = list(map(str, sorted(c)))
conv = ''.join(list_s)
result = f'"{conv}"'
print(result)