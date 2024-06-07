# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:

# Input: left = 47, right = 85
# Output: [48,55,66,77]
 

def is_self_dividing(number):
    original_number = number
    for digit_str in str(original_number):
        digit = int(digit_str)
        if digit == 0 or original_number % digit != 0:
            return False
    return True

def self_dividing_numbers(left, right):
    result = []
    for number in range(left, right + 1):
        if is_self_dividing(number):
            result.append(number)
    return result

# Examples
left1, right1 = 1, 22
print(self_dividing_numbers(left1, right1))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

left2, right2 = 47, 85
print(self_dividing_numbers(left2, right2))  # Output: [48, 55, 66, 77]
