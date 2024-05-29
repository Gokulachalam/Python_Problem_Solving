# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.



s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
 

m = s.format_map(indices)

print(m)

for m in indices:
    print(m)
