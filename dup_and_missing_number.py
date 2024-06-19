from collections import Counter
nums = [1,2,2,4]
dup = []
c =Counter(nums)

for key,value in c.items():
    if value>1:
        dup.append(key)


for j in range(1,len(nums)+1):
    if j not in nums:
        dup.append(j)
print(dup)