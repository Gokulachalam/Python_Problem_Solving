

from collections import Counter
nums = [3,3,7,7,10,11,11]
new = []
v = 0

c = Counter(nums)

for key , value in c.items():
            
            if value ==1:

                new.append(key)


                for k in range(len(new)):
                        print(new[k])
                