# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]





n = 20
result = []

for i in range(1, n + 1):
    if i % 15 == 0:
        result.append("fizzbuzz")
    elif i % 3 == 0:
        result.append("fizz")
    elif i % 5 == 0:
        result.append("buzz")
    else:
        result.append(str(i))  # Convert the number to a string

# Print the result array in the desired format
formatted_result = '["' + '","'.join(result) + '"]'
print(formatted_result)
