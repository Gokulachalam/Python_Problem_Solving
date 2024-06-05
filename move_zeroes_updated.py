# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

nums = [0,1,2,0,3,0,4,5]
cop = nums.copy()
new = []
a=[]
for i in range(len(nums)):
    if nums[i] == 0:
        new.append(nums[i])

for j in new:
    if new[j] in cop:
        cop.remove(new[j])

# print(new)
# print(cop)
c = cop+new
print(c)