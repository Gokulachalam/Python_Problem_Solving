
 
from collections import Counter
nums = [1,3,6,4,3,4,2,4,5,3,53,3,5,35,34,35,5,31,99,99]
c=Counter(nums)

new = []

for key,value in c.items():
    if value ==1:
        new.append(key)
print(max(new))


#new change