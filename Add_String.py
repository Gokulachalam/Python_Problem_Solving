# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"


num1 = "11"
num2 = "123"

conv = int(num1)
convs = int(num2)

adds = conv+convs
reconv = f'"{adds}"'
print(reconv)