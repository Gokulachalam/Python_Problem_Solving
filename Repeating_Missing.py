

# Example 1:

# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
# Example 2:

# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].

# from collections import Counter

# import itertools
# grid = [[1,3],[2,2]]
# final = []
# new=[]
# last=[]
# flattened_list = list(itertools.chain(*grid))
# print(flattened_list)

# # n = len(grid)*len(grid)

# c = Counter(flattened_list)
# print(c)

# for key,value in c.items():
#     new.append(value)
#     ma = max(new)

#     if ma==value:
#         last.append(key)

# print(last)

# maxi = max(flattened_list)
# mini = min(flattened_list)
# e = []
# for i in range(1,len(flattened_list)+1):
#     if i not in flattened_list:
#         final.append(i)
# print(final)


# for i in flattened_list:
#     for j in range(1,len(flattened_list)):
#         if flattened_list[i] == flattened_list[j]:

#             final.append(flattened_list[i])
# print(final)


# print(new)
# print(c)





# from collections import Counter
# nums =[9,1,7,8,9,2,3,4,6]
# c = Counter(nums)
# print(c)
# new =[]
# arr=[]
# for key , value in c.items():
#     if value ==2:

#         new.append(key)
# print(new)



# a=[]
# b=[]

# for u in range(1,len(nums)+1):
#     a.append(u)
#     a.sort()

# print(a)

# for l in nums:
#     b.append(l)
#     b.sort()
# print(b)


# for m in a:
#         if m not in b:
#              new.append(m)
# print(new)
         





from collections import Counter

import itertools
grid = [[9,1,7],[8,9,2],[3,4,6]]
one =[]

flattened_list = list(itertools.chain(*grid))

c = Counter(flattened_list)


for key,value in c.items():
    if value ==2:
        one.append(key)



sec = []
third = []
for j in range(1,len(flattened_list)+1):
    sec.sort()
    sec.append(j)
for k in flattened_list:
        third.sort()
        
        third.append(k)
        

for a in sec:
     if a not in third:
          one.append(a)
          

 
print(one)