# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.



n = 99
new=[]


for i in range(1,n+1):
    if n%i==0 and i!=n:
        new.append(i)
s = sum(new)
if s == n:
    print("true")
else:
    print("false")