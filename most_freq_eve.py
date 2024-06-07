# Example 1:

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.
# Example 2:

# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.
# Example 3:

# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.


from collections import Counter
nums =[10000]
print(len(nums))
new=[]
vals=[]
keys=[]
for i in range(len(nums)):

    if nums[i]%2 ==0:
        new.append(nums[i])
        for j in range(len(new)):
            for k in range(j+1,len(new)):
                if new[j] == new[k]:
                    vals.append(new[k])
print(min(vals))
#         c = Counter(nums)
# for key,value in c.items():
#     vals.append(value)
#     maxi = max(vals)

#     # if value == maxi:
#     #     keys.append(key)
    
#     #     print(keys)


# print(maxi)