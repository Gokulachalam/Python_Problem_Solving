
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[4] = -1 + 0 + 1 = 0.
# nums[0] + nums[2] + nums[3] = -1 + 1 + 2 = 2.

nums = [-1,0,1,2,-1,-4]
ans = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                print(nums[i],nums[j],nums[k])
                # ans.append(nums[i]+nums[j]+nums[k])
                # ans.sort()
                # print(ans)
                # print(i,j,k)




# Output: [[-1,-1,2],[-1,0,1]]