# Example 1:

# Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

# Output: 5

# Explanation:

# The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
# Example 2:

# Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

# Output: 2

# Explanation:

# The 2 good pairs are (3, 0) and (3, 1).

nums1 = [1,2,4,12]
nums2 = [2,4]
k = 3
new=[]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        mul=nums2[j]*k

        if nums1[i]%mul ==0:
            new.append(nums1[i])
            new.append(nums2[j])
print(new)
print(int(len(new)/2))


