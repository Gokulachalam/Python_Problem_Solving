# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# haystack = "sadbutsad" 
# needle = "sad"
# conv = [haystack]
# for i in conv:
#     if needle in haystack:
#         print("0")
#     else:
#         print("-1")




#my methd but can't print the index
haystack = "sadbutsad" 
needle = "sad"


for i in range(len(haystack)):
    for j in range(len(needle)):
        if haystack[i] == needle[j]:
            print(i)


# haystack = "sadbutsad" 
# needle = "sad"


# index = haystack.find(needle)

# print(index)
