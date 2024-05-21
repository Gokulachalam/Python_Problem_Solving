# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"



num1 = "2"
num2 = "3"
conv = int(num1)
conv1 = int(num2)
mul = conv*conv1
final_conv = str(mul)
quoted_number_str = ''.join(['"', final_conv, '"'])
print(quoted_number_str)



