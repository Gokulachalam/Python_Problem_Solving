# # # Example 1:

# # # Input: nums = [1,2,2,3,1,4]
# # # Output: 4
# # # Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# # # So the number of elements in the array with maximum frequency is 4.
# # # Example 2:

# # # Input: nums = [1,2,3,4,5]
# # # Output: 5
# # # Explanation: All elements of the array have a frequency of 1 which is the maximum.
# # # So the number of elements in the array with maximum frequency is 5.



# # from collections import Counter
# # nums = [7, 8, 7, 8, 9, 9]


# # new =[]

# # # c = Counter(nums)
# # # print(c)
# # # for key , value in c.items():
# # #     new.append(value)
# # #     m = max(new)

# # #     if value==m:
# # #         print(key)


# # for i in range(len(nums)):
# #     for j in range(i+1,len(nums)):
# #         if nums[i] == nums[j] and i!=j:

# #             new.append(nums[i])
# #             new.append(nums[j])

# # print(len(new))



# def getResult(A, n):
#     # A is the array of N elements
#     for num in A:
#         roman_num = convert_to_roman(num)
#         is_pal = is_palindrome(roman_num)
#         print('true' if is_pal else 'false')

# def is_palindrome(num_str):
#     return num_str == num_str[::-1]

# def convert_to_roman(num):
#     roman_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
#     roman_str = ''
#     for value, symbol in sorted(roman_map.items(), reverse=True):
#         count = num // value
#         roman_str += (symbol * count)
#         num -= value * count
#     return roman_str

# - def main ():
# n = int (input())
# A = []
# temp = input (). split()
# for t in temp:
# A. append (int (t))
# for t in temp:
# getResult(A, n)
# main( )

# if __name__ == '__main__':
#     main()


# def highest_possible_number(n):
#     # Convert the number to a string to manipulate digits
#     digits = list(str(n))
    
#     # Sort the digits in descending order
#     digits.sort(reverse=True)
    
#     # Join the sorted digits and convert back to integer
#     highest_number = int(''.join(digits))
    
#     return highest_number

# # Test cases
# test_cases = [786, 912345678, 100000001, 987654321, 111222333]

# for n in test_cases:
#     print(f"Input: {n} -> Output: {highest_possible_number(n)}")


# def getResult(A, n):
#     for num in A:
#         roman_num = convert_to_roman(num)
#         is_pal = is_palindrome(roman_num)
#         print('true' if is_pal else 'false')

# def is_palindrome(num_str):
#     return num_str == num_str[::-1]

# def convert_to_roman(num):
#     roman_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
#     roman_str = ''
#     for value, symbol in sorted(roman_map.items(), reverse=True):
#         count = num // value
#         roman_str += (symbol * count)
#         num -= value * count
#     return roman_str

# def main():
#     n = int(input())
#     A = []
#     temp = input().split()
#     for t in temp:
#         A.append(int(t))
#     getResult(A, n)

# if __name__ == '__main__':
#     main()



def getResult(A, n):
    for num in A:
        roman_num = convert_to_roman(num)
        is_pal = is_palindrome(roman_num)
        print('true' if is_pal else 'false')

def is_palindrome(string):
    return string == string[::-1]

def convert_to_roman(num):
    roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                 (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman_str = ''
    for value, symbol in roman_map:
        count = num // value
        roman_str += symbol * count
        num %= value
    return roman_str

def main():
    n = int(input())
    A = list(map(int, input().split()))
    getResult(A, n)

if __name__ == '__main__':
    main()