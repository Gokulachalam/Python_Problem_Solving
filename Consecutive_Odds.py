# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

# Example 1:

# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:

# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.

#edfghj


# arr = [1,3,5,24]
# new = []
# idxodd_count = 0
# for i in range(len(arr)):
#     for j in range(len(arr),i+1):
#         for k in range(len(arr),j+1):
#             if arr[i] %2!= 0 and arr[j] %2 != 0 and arr[k] %2 != 0:
#                 new.append(i)
# print(new)

# arr = [3, 5, 7, 2, 4, 6, 41]
# new = []
# idx = []
# for i in range(len(arr) - 2):
#     for j in range(i + 1, i + 2):
#         for k in range(j + 1, j + 2):
#             if arr[i] % 2 != 0 and arr[j] % 2 != 0 and arr[k] % 2 != 0:
#                 new.append(i)
#                 new.append(j)
#                 new.append(k)
#                 print(i, j, k)

# Input array
arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
found = False
for i in range(len(arr)-2):
    if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
        found = True
        print(found)