# Example 1:

# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
# Example 2:

# Input: num = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".




nums = "5400"

rev = nums[::-1]
new=[]
conv = [rev]
print(type(conv))

for i in conv:
    if conv[i] == 0:
        print(i)
