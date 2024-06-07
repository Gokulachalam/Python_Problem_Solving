# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

s = "abbca"
c = list(s)
new=[]

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if c[i] == c[j]:
            new.append(c[i])
print(new)