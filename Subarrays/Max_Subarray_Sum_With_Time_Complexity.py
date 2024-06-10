# arr = [1, 2, 3, 4]
# n = len(arr)

# # Generate all possible subarrays
# for i in range(n):
#     for j in range(i+1, n):
#         subarray = arr[i:j+1]
#         print(f"Subarray from index {i} to {j}: {subarray}")







# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.



nums = [1,2,3,4,5]
org_subarray = []
n = len(nums)
sub_sum = []
for i in range(n):
    for j in range(i,n):
        sub = nums[i:j+1]
        org_subarray.append(sub)
# print(org_subarray)


for individual in range(len(org_subarray)):
    sub_sum.append(sum(org_subarray[individual]))
    max_sum = max(sub_sum)

#     max_index = sub_sum.index(max_sum)
#     max_subarray = org_subarray[max_index]

# print(max_subarray)
print(max_sum)




