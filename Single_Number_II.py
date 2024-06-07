# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99




# from collections import Counter

# nums = [2,1,2]
# count_dict = Counter(nums)
# print(count_dict)

# for key,value in count_dict.items():
#     if value == 1:
#         print(key)





from collections import Counter
arr= [0,1,0,1,0,1,99]
count_dict = Counter(arr)

for key , value in count_dict.items():
    if value==1:
        print(key)
        