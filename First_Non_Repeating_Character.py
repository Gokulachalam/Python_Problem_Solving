# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# from collections import Counter
# s = "loveleetcode"
# a=0

# conv = [s]
# print(s)

# v = []
# for i in s:
#     if s.count(i)==1:
#         v.append(i)
# print(v)






# s = "aabb"

# v = []
# for i in s:
#     if s.count(i) == 1:
#         v.append(i)

# if v:
#     first_index = s.index(v[0])
#     print(first_index)
# else:
#     print("-1")





from collections import Counter
s = "loveleetcode"
c = Counter(s)

for i,f in enumerate(s):
    print(i,f)
