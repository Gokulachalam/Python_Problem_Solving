# Example 2:

# Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
# Output: 0
# Explanation: There are no strings that appear in each of the two arrays.
# Example 3:

# Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
# Output: 1
# Explanation: The only string that appears exactly once in each of the two arrays is "ab".


from collections import Counter
words1 = ["a","ab"]
words2 = ["a","a","a","ab"]
c = Counter(words1)
b = Counter(words2)
print(c)
print(b)
new=[]

for key,value in c.items():
    for keys,values in b.items():
        if value and value ==1:
            new.append(key)
            new.append(keys)
print(new)

# new =[]
# for i in range(len(words1)):
#     print(words1[i])
#     for j in range(len(words2)):
#         print(words2[j])
#         if words1[i] == words2[j]:
#             new.append(words1[i])
#             new.append(words2[i])

# print(new)