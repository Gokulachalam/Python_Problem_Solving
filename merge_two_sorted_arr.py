# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]



# arr1 = [1,2,4]

# arr2 = [1,3,4]

# merged_arr = arr1+arr2
# print(merged_arr)
# sort_arr = merged_arr.sort()
# print(merged_arr)



# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# num = 121
# digits = [int(digit) for digit in str(num)]  # List comprehension to convert each character to an integer
# for i in range(len(digits)-1):
#     if digits[i] == digits[i+1] and digits[i+1] == digits[i]:
#         print("yes")
#     else:
#         print("no")



# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# haystack = "sadbutsad"
# needle = "Sad"
# for char in haystack:
#     if needle.lower() in haystack.lower():
#         print(haystack[char])
#         print("yes")



# # Define the haystack and the needle
# haystack = "sadbutsad"
# needle = "sad"

# # Find the index of the first occurrence of the needle in the haystack
# index = haystack.find(needle)                                               

# # Check if the needle was found
# if index != -1:
#     print(f"The needle '{needle}' is found at index {index} in the haystack.")
# else:
#     print(f"The needle '{needle}' is not found in the haystack.")





# haystack = "sadbutsad"
# needle = "Sad"

# # Check if `needle` is in `haystack` ignoring the case
# if needle.lower() in haystack.lower():
#     print('yes')
# else:
#     print('no')




# result = []
# input_list = [1,2,1,2,1,2,3,4]
# for i in input_list:
#     if i not in result:
#         result.append(i)
        
# print(result)
# print(i.coff)
# print(result)

#     result = []
#     for item in input_list:
#         if item not in result:
#             result.append(item)
#     return result

# # Example usage
# input_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
# output_list = remove_duplicates(input_list)
# print(output_list)





# Finding the difference between the sum of odd and even numbers from a list of 5 number


# input 1 : 5
 
# input 2 : 10 11 7 12 14
# Output
# -18

n = int(input("Enter the size of the array: "))

# Initialize an empty list for arr
arr = []

# Get the array elements from the user
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

even = []
odd = []
even_tot = 0
odd_tot = 0
for i in range(len(arr)):
    if arr[i]%2 ==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
even_tot = sum(even)
odd_tot = sum(odd)
# print(even_tot)
print(odd_tot-even_tot)


