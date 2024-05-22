# arr1 = [1, 2, 3,6]
# arr2 = [3, 2, 4,5]


# # # small1 = min(arr1)
# # # small2 = min(arr2)
# # # print(small1)
# # # print(small2)
# # # for i in range(len(arr1)):
# # #     for j in range(len(arr2)):
# # #         if arr2[i] == arr1[i]:
# # #             print(i)
        



# set1 = set(arr1)
# set2 = set(arr2)

# inter = set1.intersection(set2)

# print(min(inter))


nums1=[1,2,3]
nums2=[4,5,2]
set1 = set(nums1)  # Convert the first list to a set
set2 = set(nums2)  # Convert the second list to a set
inter = set1.intersection(set2)
print(min(inter))  