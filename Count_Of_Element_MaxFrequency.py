
 
# from collections import Counter
# nums = [1,2,3,4,4,4]
# # c=Counter(nums)

# # new = []

# # print(type(c))

# # for key,value in c.items():
# new = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             new.append(nums[i])
#             new.append(nums[j])

            

# print(new[0])

def find_max_repeating_element(arr):
    # Create a dictionary to store the frequency of each element
    frequency_dict = {}

    # Traverse the array and populate the frequency dictionary
    for elem in arr:
        if elem in frequency_dict:
            frequency_dict[elem] += 1
        else:
            frequency_dict[elem] = 1

    # Find the element with the maximum frequency
    max_count = -1
    max_elem = None

    for elem, count in frequency_dict.items():
        if count > max_count:
            max_count = count
            max_elem = elem

    return max_elem

nums = [1,2,3,4,4,4]